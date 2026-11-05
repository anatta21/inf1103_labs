
from product_oop import Product


class DigitalProduct(Product):
    """A product delivered digitally."""

    TYPE = "digital"

    def __init__(self, product_id, name, price, stock_quantity, download_size):
        super().__init__(product_id, name, price, stock_quantity)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def display_information(self):
        super().display_information()
        print(
            f"   Type: Digital | Download size: "
            f"{self.__download_size} MB"
        )

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self.__download_size
        return data
