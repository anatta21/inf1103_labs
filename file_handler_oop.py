import json
import os

from inventory_oop import Inventory
from product_oop import Product


def load_inventory(filename):
    """Loads inventory data if it exists; otherwise returns an empty Inventory."""
    inventory = Inventory()
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                print("inventory.json found.")
                data = json.load(file)
            for item in data:
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"]))
            print("Inventory loaded successfully.\n")
        except (json.JSONDecodeError, OSError, KeyError):
            return Inventory()
    else:
        print("inventory.json not found!\nSuccessfully created a new inventory...\n")
    return inventory


def save_inventory(inventory, filename, is_exit=False):
    """Saves the inventory to a JSON file."""
    if not is_exit:
        print("\nSaving inventory...")
    else:
        print("\nSaving inventory before exit...")

    # JSON can't store Product objects, so convert each one to a dict
    data = [{"id": p.get_product_id(), "name": p.get_name(),
             "price": p.get_price(), "stock": p.get_stock()}
            for p in inventory.get_products()]
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        if not is_exit:
            print("Inventory saved successfully to inventory.json.\n")
        else:
            print("Inventory saved successfully.\n")
    except OSError:
        pass

#Testing
if __name__ == "__main__":
    inv = load_inventory("inventory.json")
    inv.display_all()
    inv.search_product("123").update_stock(5)
    save_inventory(inv, "test_output.json")
