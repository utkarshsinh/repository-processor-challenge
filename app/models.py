schema = {
    "type": "object",
    "properties": {
        "retailer": {"type": "string"},
        "purchaseDate": {"type": "string"},
        "purchaseTime": {"type": "string"},
        "total": {"type": "string"},
        "items": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "shortDescription": {"type": "string"},
                    "price": {"type": "string"},
                },
                "required": ["shortDescription", "price"],
            },
        },
    },
    "required": ["retailer", "purchaseDate", "purchaseTime", "total", "items"],
}

receipt_store = {}
