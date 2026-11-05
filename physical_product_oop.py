from product_oop import Product


class PhysicalProduct(Product):
    """A product that is stored and shipped. Weight is in kg."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"   Type: Physical | Weight: {self.__weight} kg")

#Test
if __name__ == "__main__":
    # Runs only when you execute this file directly, not when it is imported
    guitar = PhysicalProduct("P001", "Guitar", 499.99, 5, 3.5)
    guitar.display_information()
