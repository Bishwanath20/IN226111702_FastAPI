from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Product list (sample data)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to My E-commerce Store API"}

# Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Filter products by category
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    result = [
        p for p in products
        if p["category"].lower() == category_name.lower()
    ]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

# Show in-stock products
@app.get("/products/instock")
def get_instock_products():

    instock = [
        p for p in products if p["in_stock"]
    ]

    return {
        "available_products": instock,
        "count": len(instock)
    }

# Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)
    in_stock = len([p for p in products if p["in_stock"]])
    out_of_stock = total_products - in_stock

    categories = list(set(p["category"] for p in products))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

# Search products
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    result = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    return {
        "keyword": keyword,
        "results": result,
        "count": len(result)
    }

# Cheapest and most expensive product
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }