import os # Lets Python interact with the operating system. "Does this file exist on the computer?”
import csv # Allows Python to read and write CSV files (comma-separated values).
from datetime import datetime # Gives you access to the current date and time.

def view_transaction_history(user, limit=10):

    return user.get("transactions", [])[-limit:]
# Returns the last 10 transactions the user has made.

def export_transaction_history(user, directory="exports"):

    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f"{user['username']}_transactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    path = os.path.join(directory, filename)

    transactions = user.get("transactions", [])

    if not transactions:
        raise ValueError("No transactions to export")

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)

    return path

# It's supposed to export all user's transaction history to a file but im not even sure it works 

def generate_summary_report(users):
    
    total_deposits = 0
    total_withdrawals = 0
    transaction_count = 0

    for user in users.values():
        for txn in user.get("transactions", []):
            transaction_count += 1
            if txn["type"] in ("deposit", "transfer_in", "interest"):
                total_deposits += txn["amount"]
            elif txn["type"] in ("withdrawal", "transfer_out", "fees"):
                total_withdrawals += txn["amount"]

    avg_transaction = (
        (total_deposits + total_withdrawals) / transaction_count
        if transaction_count > 0 else 0
    )

    return {
        "total_deposits": round(total_deposits, 2),
        "total_withdrawals": round(total_withdrawals, 2),
        "average_transaction": round(avg_transaction, 2),
        "transaction_count": transaction_count
    }
    
# Made this for the admin panel, but couldn't really get around to doing that. So this function is just sitting there 

def total_bank_balance(users):
    
    return round(sum(user.get("balance", 0) for user in users.values()), 2)
    
# Unused Admin panel code.

def list_high_value_customers(users, threshold):
   
    return [
        user["username"]
        for user in users.values()
        if user.get("balance", 0) >= threshold
    ]
# Another unused admin panel code, 





