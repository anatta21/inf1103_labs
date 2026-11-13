from product_oop import Product


class OrderLine:
    """Represents a product and its quantity in an order."""

    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal for this order line."""

        return self.product.price * self.quantity
