from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
    
    
    
# Separation of Concerns:

# The Product class encapsulates product data, while the functions handle interactions with the dao layer. This separation is good for maintainability.
# Static Method for Object Loading:

# Using the @staticmethod load to create a Product instance from a dictionary ensures flexibility and minimizes repetitive code.