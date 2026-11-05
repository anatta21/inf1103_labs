from product_oop import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    """A product that requires physical delivery."""

    TYPE = "physical"

    def __init__(self, product_id, name, price, stock_quantity, weight):
        super().__init__(product_id, name, price, stock_quantity)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2.50

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def display_information(self):
        super().display_information()
        print(f"   Type: Physical | Weight: {self.__weight} kg")
        print(f"   Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data
