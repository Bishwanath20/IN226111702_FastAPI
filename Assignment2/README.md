FastAPI Internship Training — Day 2 Assignment
Project Overview

This project is a continuation of my FastAPI Internship Training (Day 2).

On Day 1, I built a simple E-commerce API with basic GET endpoints to view and filter products.

On Day 2, I expanded the project by adding more practical backend features such as:

Filtering products using query parameters

Validating request data using Pydantic

Creating POST APIs to send data to the server

Updating data using PATCH APIs

Implementing a simple order tracking system

These additions help simulate how real-world backend APIs handle user input, validation, and data updates.

Key Concepts Learned
Query Parameters

Query parameters allow users to filter results directly through the URL.

Example:

/products/filter?category=Electronics

Users can also filter by price range:

/products/filter?min_price=100&max_price=1000
Data Validation with Pydantic

FastAPI uses Pydantic models to validate incoming data.

For example, in the feedback system:

Customer name must have a minimum length

Product ID must be positive

Rating must be between 1 and 5

Comments are optional

This ensures the API only accepts valid and structured data.

API Endpoints
1. Filter Products

GET /products/filter

Filters products using optional parameters:

category

min_price

max_price

Example:

/products/filter?category=Electronics
2. Get Product Price

GET /products/{product_id}/price

Returns only the name and price of a product.

Example response:

{
 "name": "Notebook",
 "price": 99
}
3. Customer Feedback System

POST /feedback

Allows customers to submit feedback for a product.

Example request:

{
 "customer_name": "Kavya",
 "product_id": 1,
 "rating": 5,
 "comment": "Great product"
}

The request data is validated using Pydantic models.

4. Product Summary Dashboard

GET /products/summary

Provides a quick overview of the store including:

Total products

Products in stock

Products out of stock

Most expensive product

Cheapest product

Available categories

This endpoint is useful for admin dashboards or analytics.

5. Bulk Order System

POST /orders/bulk

Allows companies to place bulk orders containing multiple products.

Example request:

{
 "company_name": "Tech Corp",
 "contact_email": "tech@corp.com",
 "items": [
   {"product_id": 1, "quantity": 5},
   {"product_id": 2, "quantity": 3}
 ]
}

The API checks:

If products exist

If they are in stock

The response returns confirmed items, failed items, and total order cost.

Bonus Feature — Order Status Tracker
Place Order

POST /orders

Creates a new order with status:

pending
View Order

GET /orders/{order_id}

Returns the details of a specific order.

If not found:

{"error": "Order not found"}
Confirm Order

PATCH /orders/{order_id}/confirm

Updates order status:

pending → confirmed

This simulates how real systems process orders.

Key Takeaways

Through this assignment, I learned how to:

Use query parameters to filter API results

Validate input data using Pydantic

Create POST APIs

Update resources using PATCH APIs

Build simple order workflows

These concepts are essential for real-world backend development.

Technologies Used

Python

FastAPI

Pydantic

Uvicorn

Swagger UI
