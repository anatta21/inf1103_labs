import json
import os

from digital_product import DigitalProduct
from inventory_oop import Inventory
from physical_product import PhysicalProduct


def create_product(item):
    """Build the right Product subclass from a saved dict, using its 'type'."""
    # Lab 6 files have no "type"; treat them as physical with unknown (0) weight.
    product_type = item.get("type", PhysicalProduct.TYPE)
    if product_type == PhysicalProduct.TYPE:
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], item.get("weight", 0.0))
    if product_type == DigitalProduct.TYPE:
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], item["download_size"])
    raise ValueError(f"Unknown product type: {product_type}")

def load_inventory(filename):
    """Loads inventory data if it exists; otherwise returns an empty Inventory."""
    inventory = Inventory()
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                print("inventory.json found.")
                data = json.load(file)
            for item in data:
                inventory.add_product(create_product(item))
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
