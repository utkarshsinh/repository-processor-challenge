Setting up a virtual environment is a recommended practice to manage dependencies and avoid conflicts with other projects, but it is not strictly necessary if it worked without it. You can remove that step if you prefer.

As for Python 3.9, it's just an example. The application should work with any Python 3.x version that supports the required libraries. If you have a different version, you can use that.

Here’s an updated README without the virtual environment setup and specifying Python 3.x:

---

# Receipt Processor

## Overview
This application processes receipts and calculates points based on specified rules. It provides two main endpoints:
- `POST /receipts/process`: Processes a receipt and returns an ID.
- `GET /receipts/{id}/points`: Returns points for a given receipt ID.

## Prerequisites
- Python 3.x
- Docker (optional, for Docker setup)

## Running Locally

### 1. Clone the Repository
```sh
git clone https://github.com/utkarshsinh/receipt-processor.git
cd receipt-processor
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Application
```sh
python -m app.routes
```

The service will be available at `http://localhost:6000`.

## Running with Docker

### 1. Build the Docker Image
```sh
docker build -t receipt-processor .
```

### 2. Run the Docker Container
```sh
docker run -p 6000:6000 receipt-processor
```

The service will be available at `http://localhost:6000`.

## Endpoints

### 1. Process Receipt
- **URL**: `http://localhost:6000/receipts/process`
- **Method**: POST
- **Payload**:
  ```json
  {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "total": "35.35",
    "items": [
      {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "id": "some-unique-id"
  }
  ```

### 2. Get Points
- **URL**: `http://localhost:6000/receipts/{id}/points`
- **Method**: GET
- **Response**:
  ```json
  {
    "points": 28
  }
  ```

## License
This project is licensed under the MIT License.

---

This README provides clear instructions on how to set up and run the application both locally and using Docker without the virtual environment setup. If you have any further questions or need additional modifications, feel free to ask!
