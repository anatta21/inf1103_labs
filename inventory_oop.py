class Inventory:
    """Manage a collection of Products."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Returns False if the ID already exists."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the Product with a matching ID (case-insensitive), else None."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("-" * 40)
        print("Current Inventory")
        for product in self.__products:
            product.display_information()
        print("-" * 40 + "\n")

    def get_products(self):
        # A copy, so callers can't modify the internal list
        return list(self.__products)

#Testing inventory file
if __name__ == "__main__":
    from product_oop import Product

    inventory = Inventory()
    inventory.add_product(Product("P001", "Laptop", 1200.0, 15))
    inventory.add_product(Product("P002", "Mouse", 25.5, 40))
    print(inventory.add_product(Product("p001", "Duplicate", 1.0, 1)))  # False
    inventory.display_all()

    found = inventory.search_product("p002")
    found.update_stock(10)
    inventory.display_all()
    print(inventory.search_product("P999"))  # None
