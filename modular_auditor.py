"""
Changed the coding structure to pure functions
"""

TAX_RATE = 0.10  # 10% tax per delivery


def get_valid_input():
   
    user_input = input("Enter the inventory count OR type 'quit' to exit: ").strip()

    if user_input.lower() == "quit":
        return None, "quit"

    try:
        value = int(user_input)
        if value < 0:
            print("Error: Negative numbers are not allowed.")
            return None, "invalid"
        return value, "ok"
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None, "invalid"


def process_delivery(current_total, new_value):
    """
    In:  current_total (int), new_value (int)
    Out: updated running total (int)
    """
    return current_total + new_value


def calculate_tax(amount):
    """
    In:  amount (int) — a single delivery's quantity
    Out: tax owed on that delivery (float)
    """
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts):
    """
    In:  total_units (int), failed_attempts (int)
    Out: None — this is the one function allowed to print, so if the
         manager later wants the report written to a file instead, only
         this function needs to change.
    """
    print("\n------- Inventory Report -------")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    inventory_count = 0
    failed_entries = 0

    while True:
        value, status = get_valid_input()

        if status == "quit":
            break
        elif status == "invalid":
            failed_entries += 1
            continue
        else:  # "ok"
            inventory_count = process_delivery(inventory_count, value)
            tax = calculate_tax(value)
            print(f"\nCurrent Total Inventory: {inventory_count}")
            print(f"Tax for this delivery: {tax:.2f}")

            if inventory_count > 500:
                print("\n*** OVERSTOCK ALERT: Total inventory has exceeded 500 units! ***")
                break

    generate_report(inventory_count, failed_entries)


if __name__ == "__main__":
    main()