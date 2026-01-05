from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import uuid

MIN_BALANCE = Decimal("0.00")



def _round(amount):
    return Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def _new_transaction(txn_type, amount, balance_after, channel):
    return {
        "id": str(uuid.uuid4()),
        "type": txn_type,
        "amount": float(amount),
        "balance_after": float(balance_after),
        "channel": channel,
        "timestamp": datetime.now().isoformat()
    }
# Helps keeping track of the transactions.


def deposit_money(user, amount, channel="branch"): 
    amount = _round(amount)

    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    balance = _round(user["balance"])
    balance += amount
    user["balance"] = float(balance)

    txn = _new_transaction("deposit", amount, balance, channel)
    user["transactions"].append(txn)

    return user
# Magically makes money out of thin air and deposits it to your account.




def withdraw_money(user, amount, channel="branch"):
    amount = _round(amount)

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    balance = _round(user["balance"])

    if balance - amount < MIN_BALANCE:
        raise ValueError("Insufficient funds")

    balance -= amount
    user["balance"] = float(balance)

    txn = _new_transaction("withdrawal", amount, balance, channel)
    user["transactions"].append(txn)

    return user
# Makes a withdrawal. What else would it do??



def transfer_funds(users, sender_username, receiver_username, amount):
    if sender_username not in users:
        raise ValueError("Sender does not exist")

    if receiver_username not in users:
        raise ValueError("Receiver does not exist")

    amount = _round(amount)
    sender = users[sender_username]
    receiver = users[receiver_username]

    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    sender_balance = _round(sender["balance"])
    if sender_balance - amount < MIN_BALANCE:
        raise ValueError("Insufficient funds")

    
    sender_balance -= amount
    sender["balance"] = float(sender_balance)
    sender["transactions"].append(
        _new_transaction("transfer_out", amount, sender_balance, "transfer")
    )

    
    receiver_balance = _round(receiver["balance"]) + amount
    receiver["balance"] = float(receiver_balance)
    receiver["transactions"].append(
        _new_transaction("transfer_in", amount, receiver_balance, "transfer")
    )

    return sender, receiver
# Helps you give money to your broke ahh friends. 



def check_balance(user):
    return float(_round(user["balance"]))

# Shows you how much money you be stacking.







