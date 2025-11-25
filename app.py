from fastapi.responses import FileResponse
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int | None = None
    name: str
    price: float

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mobile", "price": 30000}
]

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    return product if product else {"error": "Product not found"}

@app.post("/api/products")
def add_product(product: Product):
    new_id = max(p["id"] for p in products) + 1
    product.id = new_id
    products.append(product.dict())
    return product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    global products
    filtered = [p for p in products if p["id"] != product_id]
    if len(filtered) == len(products):
        return {"error": "Product not found"}
    products = filtered
    return {"message": "Deleted"}

@app.get("/")
def serve_homepage():
    return FileResponse("index.html")

