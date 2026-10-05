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


