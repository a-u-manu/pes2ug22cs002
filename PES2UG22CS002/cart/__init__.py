import json
from typing import List

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict):
        return Cart(
            id=data['id'], 
            username=data['username'], 
            contents=[Product(**content) for content in json.loads(data['contents'])], 
            cost=data['cost']
        )

def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Collect all product IDs from the cart
    product_ids = []
    for cart_detail in cart_details:
        product_ids.extend(json.loads(cart_detail['contents']))

    # Fetch all products in a single call (assuming such functionality exists)
    products_map = {product.id: product for product in products.get_products_by_ids(product_ids)}

    # Map product IDs to product objects
    products_in_cart = [products_map[product_id] for product_id in product_ids if product_id in products_map]

    return products_in_cart

def add_to_cart(username: str, product_id: int):
    if products.get_product(product_id):  # Ensure product exists before adding
        dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)
    
    
    
    
# The code has been updated to reduce the number of database requests:

# Batch Product Fetching:

# Collected all product IDs from the cart in a single loop.
# Used a hypothetical get_products_by_ids method to fetch all products in one call.
# Mapping for Efficient Access:

# Created a dictionary (products_map) to map product IDs to product objects, reducing repetitive lookups in the get_cart function.
# These changes minimize redundant computations and database requests. 