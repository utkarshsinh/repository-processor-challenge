from flask import Flask, request, jsonify
from flask_expects_json import expects_json
from app.services import compute_points
from app.models import schema, receipt_store
import uuid
import threading
import os

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

# Lock for thread-safe operations
lock = threading.Lock()

@app.route("/receipts/process", methods=["POST"])
@expects_json(schema)
def process_receipt():
    data = request.get_json()
    receipt_id = str(uuid.uuid4())
    try:
        data["points"] = compute_points(data)
    except ValueError as e:
        return {"ERROR": "Invalid Receipt", "MESSAGE": str(e)}, 400

    with lock:
        receipt_store[receipt_id] = data

    return {"id": receipt_id}, 200

@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_receipt_points(receipt_id):
    try:
        with lock:
            points = receipt_store[receipt_id]["points"]
        return {"points": points}, 200
    except KeyError as e:
        return {"ERROR": "Receipt Not Found", "MESSAGE": f"Receipt ID {e.args[0]} does not exist."}, 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=False, host="0.0.0.0", port=port)
