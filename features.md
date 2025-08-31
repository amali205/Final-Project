# Endpoints

// ====================== AUTHENTICATION ======================

Endpoint: register/
Method: POST
Body:
{
  "username": "customer1",
  "email": "customer1@example.com",
  "password": "Test1234"
}
Response:
{
  "username": "customer1",
  "email": "customer1@example.com",
}

Endpoint: login/
Method: POST
Body:
{
  "username": "customer1",
  "password": "Test1234"
}
Response:
{
  "access": "jwt_access_token_here",
  "refresh": "jwt_refresh_token_here",

}

// ====================== PRODUCTS ======================

Endpoint: products/
Method: GET
Body: None
Response:
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1200,
    "stock": 10,
    "category": 1
  }
]

// ====================== CART ======================

Endpoint: cart/
Method: POST
Body:
{
  "product_id": 1,
  "quantity": 2
}
Response:
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "Laptop",
    "price": 1200
  },
  "quantity": 2,
  "total_price": 2400
}

// ====================== ORDERS ======================

Endpoint: api/orders/
Method: POST
Body: None
Response:
{
  "id": 1,
  "items": [
    {
      "product": {
        "id": 1,
        "name": "Laptop",
        "price": 1200
      },
      "quantity": 2,
      "total_price": 2400
    }
  ],
  "total_amount": 2400,
  "status": "Pending",
  "created_at": "2025-08-31T20:00:00Z"
}
