class Product:
    """Responsibility: represent and manage ONE product."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

#For Testing
if __name__ == "__main__":
    p = Product("P001", "Laptop", 1200.0, 15)
    print(p.get_name(), p.get_stock())
