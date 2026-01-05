import os
import csv
from datetime import datetime

def view_transaction_history(user, limit=10):
    """
    Return the most recent transactions (default last 10)
    """
    return user.get("transactions", [])[-limit:]


def export_transaction_history(user, directory="exports"):
    """
    Export a user's transactions to a CSV file
    """
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

# I'm not even sure this works.

def generate_summary_report(users):
    """
    Return analytics summary for all users
    """
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
    
# Made this for the admin panel, but couldn't really get around to doing that. So this function is just sitting there lmao

def total_bank_balance(users):
    """
    Return total balance held by the bank
    """
    return round(sum(user.get("balance", 0) for user in users.values()), 2)
    
# Unused Admin panel code.

def list_high_value_customers(users, threshold):
    """
    Return usernames with balances >= threshold
    """
    return [
        user["username"]
        for user in users.values()
        if user.get("balance", 0) >= threshold
    ]
# Another unused admin panel code, nothing to see here.
