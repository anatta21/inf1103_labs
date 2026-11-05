
import json
import os

from product_factory import product_from_dict


class Inventory:
    """Manages Product objects."""

    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id in self._products:
            raise ValueError("A product with that ID already exists.")

        self._products[product.product_id] = product

    def display_all(self):
        if not self._products:
            print("Inventory is empty.")
            return

        for product in self._products.values():
            product.display_information()

    def update_stock(self, product_id, change):
        product = self.find(product_id)

        if product is None:
            raise ValueError("Product not found.")

        product.update_stock(change)

    def find(self, product_id):
        return self._products.get(product_id)

    def search_by_name(self, text):
        return [
            p for p in self._products.values()
            if text.lower() in p.name.lower()
        ]

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(
                [p.to_dict() for p in self._products.values()],
                file,
                indent=4
            )

    def load(self, filename):
        if not os.path.exists(filename):
            return

        with open(filename) as file:
            data = json.load(file)

        for item in data:
            self.add_product(product_from_dict(item))
