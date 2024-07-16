from datetime import datetime
from math import ceil

def compute_points(receipt_json):
    total_points = 0
    retailer = receipt_json["retailer"]
    total_amount = float(receipt_json["total"])

    # Points for alphanumeric characters in retailer name
    total_points += sum(1 for char in retailer if char.isalnum())

    # Round dollar amount
    if total_amount.is_integer():
        total_points += 50

    # Multiple of 0.25
    if total_amount % 0.25 == 0:
        total_points += 25

    # Points for items
    items = receipt_json["items"]
    total_points += (len(items) // 2) * 5

    # Points for item descriptions
    for item in items:
        if len(item["shortDescription"].strip()) % 3 == 0:
            total_points += ceil(float(item["price"]) * 0.2)

    # Points for odd day purchase date
    purchase_date = datetime.strptime(receipt_json["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        total_points += 6

    # Points for purchase time between 2:00 PM and 4:00 PM
    purchase_time = datetime.strptime(receipt_json["purchaseTime"], "%H:%M")
    if datetime.strptime("14:00", "%H:%M") < purchase_time < datetime.strptime("16:00", "%H:%M"):
        total_points += 10

    return total_points
