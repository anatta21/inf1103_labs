from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class for all products."""

    def __init__(self, product_id, name, price, stock_quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock_quantity = stock_quantity

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock_quantity(self):
        return self._stock_quantity

    def update_stock(self, change):
        """Update product stock quantity."""
        if self._stock_quantity + change < 0:
            raise ValueError("Stock cannot go below zero.")

        self._stock_quantity += change

    def display_information(self):
        """Display common product information."""
        print(
            f"ID: {self._product_id} | "
            f"Name: {self._name} | "
            f"Price: ${self._price:.2f} | "
            f"Stock: {self._stock_quantity}"
        )

    def to_dict(self):
        """Convert common product information into a dictionary."""
        return {
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock_quantity": self._stock_quantity
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return product-specific fulfilment information."""
