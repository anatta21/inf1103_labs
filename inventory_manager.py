import json
import os

FILENAME = "inventory.json"


def load_inventory():
    """Loads inventory data if it exists; otherwise initialises an empty inventory."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                print("inventory.json found.")
                data = json.load(file)
                print("Inventory loaded successfully.\n")
                return data
        except (json.JSONDecodeError, OSError):
            return []
    else:
        print("inventory.json not found!\nSuccessfully created a new inventory...\n")
        return []

def save_inventory(inventory, is_exit=False):
    """Saves current inventory list to inventory.json."""
    if not is_exit:
        print("\nSaving inventory...")
    else:
        print("\nSaving inventory before exit...")
        
    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        
        if not is_exit:
            print("Inventory saved successfully to inventory.json.\n")
        else:
            print("Inventory saved successfully.\n")
    except OSError:
        pass

def print_menu():
    print("""----------MENU----------
1. Display All Products)
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit""")
    print("-" * 40 + "\n")



def display_all(inventory):
    """Displays all products in the inventory."""
    print("-" * 40)
    print("Current Inventory")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-" * 40 + "\n")

def add_product(inventory):
    """Adds a new product to the inventory."""
    print("Add New Product")
    prod_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": prod_id,
        "name": name,
        "price": price,
        "stock": stock,
    }
    inventory.append(new_product)
    print("\nProduct added successfully!\n")

def update_stock(inventory):
    """Updates stock quantity for an existing product."""
    print("Update Stock")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print("\nProduct Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}\n")

            new_stock = int(input("New Stock Quantity: "))
            item["stock"] = new_stock
            print("\nStock updated successfully!\n")
            return

    print("\nProduct not found.\n")

def search_product(inventory):
    """Searches for a product by ID."""
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print("\nProduct Found")
            print("-" * 40)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("-" * 40 + "\n")
            return

    print("\nProduct not found.\n")


print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40 + "\n")
inventory = load_inventory()
print_menu()

while True:
    choice = input("Enter option: ").strip()

    if choice == "1":
        display_all(inventory)
    elif choice == "2":
        add_product(inventory)
    elif choice == "3":
        update_stock(inventory)
    elif choice == "4":
        search_product(inventory)
    elif choice == "5":
        save_inventory(inventory)
    elif choice == "6":
        save_inventory(inventory, is_exit=True)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

