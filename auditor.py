inventory_count = 0
failed_entries = 0

while True:

    user_input = input("Enter the inventory count OR type 'quit' to exit: ").strip() 

    if user_input.lower() == 'quit':
        break
    try:
        stock_quantity = int(user_input) 

        if stock_quantity < 0:
            print("Error: Negative numbers are not allowed.")
            failed_entries += 1
            continue

        inventory_count += stock_quantity
        print(f"\nCurrent Total Inventory: {inventory_count}")    

        if inventory_count > 500:
            print("\n*** OVERSTOCK ALERT: Total inventory has exceeded 500 units! ***")
            break
# Handle invalid input like "one" or "90k"
    except ValueError:
        if not user_input.isdigit():
            print("Error: Invalid input. Please enter a valid integer.")
            failed_entries += 1
            continue

print("\n------- Inventory Report -------")
print(f"Total Units Processed: {inventory_count}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")