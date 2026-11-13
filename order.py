from order_line import OrderLine
from product_oop import Product


class Order:
    """Manages an order and its OrderLine objects."""

    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create and add an OrderLine to the order."""

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """Calculate the total value of the order."""

        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        """Display order details and its total."""

        print(f"\nOrder ID: {self.order_id}")
        print("--------------------------------")

        if not self.order_lines:
            print("This order has no items.")
            return

        for order_line in self.order_lines:
            product = order_line.product

            print(f"Product: {product.name}")
            print(f"Product ID: {product.product_id}")
            print(f"Price: ${product.price:.2f}")
            print(f"Quantity: {order_line.quantity}")
            print(
                f"Subtotal: ${order_line.calculate_subtotal():.2f}"
            )
            print("--------------------------------")

        print(f"Order Total: ${self.calculate_total():.2f}")
