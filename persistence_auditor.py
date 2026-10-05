"""
Week 4: File handling and transaction history 
"""

TAX_RATE = 0.10  # 10% tax per delivery
INVENTORY_FILE = "inventory.txt"

def load_inventory():
    total = 0
    history = []
    try:
        order_id = 1000 
        with open(INVENTORY_FILE, "r") as f:
            for line in f:
                if line.strip() != "":
                    print(line.strip())
                    order_id = int(line[:4])
        return order_id
    except FileNotFoundError:
        return None 

def save_inventory(order):
    with open(INVENTORY_FILE, "a+") as f:
        f.write("\n" + order)


last_id = load_inventory()
    
while True:
    if  last_id != None:
        new_id =    last_id + 1
    else:
        new_id = 1001
    last_id = new_id
    product_name = input("Enter Product Name: ").strip()
    product_quantity = int(input("Enter quantity: "))  
    current_order = f"{new_id}: {product_quantity} {product_name}(s)"
    save_inventory(current_order)

    print("New order added\n")
    print(current_order)
    print("\n\nOrder Successfully saved to inventory.txt")

    userCmd = input("Do you want to add more items? (Y/n) or Type 'quit' to end the program: ")
    if userCmd.lower() == 'n' or userCmd.lower() == "quit":
        break
