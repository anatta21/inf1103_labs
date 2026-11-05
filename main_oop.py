from digital_product import DigitalProduct
from inventory_oop import Inventory
from physical_product import PhysicalProduct

DATA_FILE = "inventory.json"


def read_number(prompt, cast=float):
    """Read and validate numeric input."""
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def add_product_flow(inventory):
    """Handle adding a physical or digital product."""

    kind = input("Type - (p)hysical or (d)igital: ").strip().lower()

    if kind not in ("p", "d"):
        print("Invalid type.")
        return

    product_id = input("Product ID: ").strip()
    name = input("Name: ").strip()

    price = read_number("Price: ", float)
    stock_quantity = read_number("Stock quantity: ", int)

    if kind == "p":
        weight = read_number("Weight (kg): ", float)

        product = PhysicalProduct(
            product_id,
            name,
            price,
            stock_quantity,
            weight
        )

    else:
        download_size = read_number("Download size (MB): ", float)

        product = DigitalProduct(
            product_id,
            name,
            price,
            stock_quantity,
            download_size
        )

    inventory.add_product(product)
    print("Product added.")


def main():
    """Main program."""

    inventory = Inventory()

    try:
        inventory.load(DATA_FILE)
        print("Inventory loaded successfully.\n")

    except (ValueError, OSError) as error:
        print(f"Error loading inventory: {error}")
        return

    while True:
        print("\n1. Display all")
        print("2. Add product")
        print("3. Update stock")
        print("4. Search product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                inventory.display_all()

            elif choice == "2":
                add_product_flow(inventory)

            elif choice == "3":
                product_id = input("Product ID: ").strip()
                change = read_number("Change (+/-): ", int)

                inventory.update_stock(product_id, change)
                print("Stock updated.")

            elif choice == "4":
                search_text = input("Name contains: ")
                results = inventory.search_by_name(search_text)

                if results:
                    for product in results:
                        product.display_information()
                else:
                    print("No matches.")

            elif choice == "5":
                inventory.save(DATA_FILE)
                print("Inventory saved successfully.")

            elif choice == "6":
                inventory.save(DATA_FILE)
                print("Saved. Goodbye!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
