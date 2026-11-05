from digital_product_oop import DigitalProduct
from file_handler_oop import load_inventory, save_inventory
from physical_product_oop import PhysicalProduct

FILENAME = "inventory.json"


def print_menu():
    print("""----------MENU----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit""")
    print("-" * 40 + "\n")


def add_product(inventory):
    print("Add New Product")
    kind = input("Type (1 = Physical, 2 = Digital): ").strip()
    if kind not in ("1", "2"):
        print("\nInvalid product type. Product not added.\n")
        return
    prod_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if kind == "1":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(prod_id, name, price, stock, weight)
        else:
            size = float(input("Download size (MB): "))
            product = DigitalProduct(prod_id, name, price, stock, size)
    except ValueError:
        print("\nInvalid number entered. Product not added.\n")
        return
    if inventory.add_product(product):
        print("\nProduct added successfully!\n")
    else:
        print("\nA product with that ID already exists.\n")

def update_stock(inventory):
    print("Update Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("\nProduct not found.\n")
        return

    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}\n")
    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("\nInvalid number entered.\n")
        return

    if product.update_stock(new_stock):
        print("\nStock updated successfully!\n")
    else:
        print("\nStock cannot be negative.\n")


def search_product(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("\nProduct not found.\n")
        return

    print("\nProduct Found")
    print("-" * 40)
    print(f"ID: {product.get_product_id()}")
    print(f"Name: {product.get_name()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Stock: {product.get_stock()}")
    print("-" * 40 + "\n")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40 + "\n")
    inventory = load_inventory(FILENAME)
    print_menu()

    while True:
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory, FILENAME)
        elif choice == "6":
            save_inventory(inventory, FILENAME, is_exit=True)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break


if __name__ == "__main__":
    main()
