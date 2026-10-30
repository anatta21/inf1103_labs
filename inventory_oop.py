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
