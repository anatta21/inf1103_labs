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


