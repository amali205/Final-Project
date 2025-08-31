# Final-Project

# E-commerce API (Django REST Framework)

This is a backend E-commerce application built with Django REST Framework.
It provides APIs for managing products, categories, carts, and orders with authentication and permissions.

# Features Implemented
🔑 Authentication & Users

Register and login users with JWT tokens.

Role-based permissions:

Admin → Full access to manage products & orders.

Customer → Can browse products, manage their cart, and place orders.

📦 Products & Categories

Admin can create, update, delete products and categories.

Customers can browse & search products.

Product fields: name, description, price, stock, and category.

🛍️ Cart

Each user has their own cart.

Add products to cart.

Update quantity of products.

Remove items from cart.

View total price in cart.

🧾 Orders

Place orders directly from cart.

View order history for each customer.

Admin can see and manage all orders.

✅ Validation & Error Handling

Prevent checkout if stock is not available.

Validate quantities and required fields.

Return proper error messages on invalid requests.

# 📬 API Endpoints (Test with Postman)

🔑 Authentication

POST /api/auth/register/ → Register new user

POST /api/auth/login/ → Login and get token


📦 Products

GET /api/products/ → List products

GET /api/products/{id}/ → Product details

POST /api/products/ (Admin only) → Create product

PATCH /api/products/{id}/ (Admin only) → Update product

DELETE /api/products/{id}/ (Admin only) → Delete product

🛍️ Cart

GET /api/cart/ → View cart

POST /api/cart/add/ → Add item to cart

PATCH /api/cart/update/{item_id}/ → Update quantity

DELETE /api/cart/remove/{item_id}/ → Remove item

🧾 Orders

POST /api/orders/ → Place order from cart

GET /api/orders/ → View user’s orders

GET /api/orders/all/ (Admin only) → View all orders