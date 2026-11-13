
from digital_product import DigitalProduct
from inventory_oop import Inventory
from physical_product import PhysicalProduct
from supplier import Supplier

DATA_FILE = "inventory.json"


def read_number(prompt, cast=float):
    """Read and validate numeric input."""

    while True:
        try:
            return cast(input(prompt))

        except ValueError:
            print("Please enter a valid number.")


def create_supplier():
    """Create a Supplier object."""

    print("\nSupplier Information")

    supplier_id = input("Supplier ID: ").strip()
    name = input("Supplier name: ").strip()
    contact_email = input("Supplier email: ").strip()

    return Supplier(
        supplier_id,
        name,
        contact_email
    )


def add_product_flow(inventory):
    """Handle adding a physical or digital product."""

    kind = input(
        "Type - (p)hysical or (d)igital: "
    ).strip().lower()

    if kind not in ("p", "d"):
        print("Invalid type.")
        return

    product_id = input("Product ID: ").strip()
    name = input("Name: ").strip()
    price = read_number("Price: ", float)
    stock_quantity = read_number("Stock quantity: ", int)

    supplier = create_supplier()

    if kind == "p":
        weight = read_number("Weight (kg): ", float)

        product = PhysicalProduct(
            product_id,
            name,
            price,
            stock_quantity,
            weight,
            supplier
        )

    else:
        download_size = read_number(
            "Download size (MB): ", float
        )

        product = DigitalProduct(
            product_id,
            name,
            price,
            stock_quantity,
            download_size,
            supplier
        )

    inventory.add_product(product)

    print("\nProduct added successfully.")


def display_inventory(inventory):
    """Display all products in the inventory."""

    print("\n========== INVENTORY ==========")

    inventory.display_all()

    print("================================")


def update_stock_flow(inventory):
    """Handle updating product stock."""

    product_id = input("Product ID: ").strip()

    change = read_number(
        "Change (+/-): ", int
    )

    inventory.update_stock(product_id, change)

    product = inventory.find(product_id)

    print("\nStock updated successfully.")
    print(f"Product: {product.name}")
    print(f"Updated stock quantity: {product.stock_quantity}")


def search_product_flow(inventory):
    """Search for products by name."""

    search_text = input("Name contains: ").strip()

    results = inventory.search_by_name(search_text)

    if results:
        print("\n========== SEARCH RESULTS ==========")

        for product in results:
            product.display_information()

    else:
        print("No matching products found.")


def save_inventory(inventory):
    """Save inventory data to JSON."""

    inventory.save(DATA_FILE)

    print(f"\nInventory saved successfully to {DATA_FILE}.")


def main():
    """Main program."""

    inventory = Inventory()

    try:
        inventory.load(DATA_FILE)
        print("Inventory loaded successfully.")

    except (ValueError, OSError) as error:
        print(f"Error loading inventory: {error}")
        print("Starting with an empty inventory.")

    while True:
        print("\n========== PRODUCT INVENTORY SYSTEM ==========")
        print("1. Display all products")
        print("2. Add product")
        print("3. Update stock")
        print("4. Search product")
        print("5. Save inventory")
        print("6. Exit")
        print("==============================================")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                display_inventory(inventory)

            elif choice == "2":
                add_product_flow(inventory)

            elif choice == "3":
                update_stock_flow(inventory)

            elif choice == "4":
                search_product_flow(inventory)

            elif choice == "5":
                save_inventory(inventory)

            elif choice == "6":
                save_inventory(inventory)
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-6.")

        except (ValueError, OSError) as error:
            print(f"Error: {error}")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
