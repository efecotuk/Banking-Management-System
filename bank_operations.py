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

    # Debit sender
    sender_balance -= amount
    sender["balance"] = float(sender_balance)
    sender["transactions"].append(
        _new_transaction("transfer_out", amount, sender_balance, "transfer")
    )

    # Credit receiver
    receiver_balance = _round(receiver["balance"]) + amount
    receiver["balance"] = float(receiver_balance)
    receiver["transactions"].append(
        _new_transaction("transfer_in", amount, receiver_balance, "transfer")
    )

    return sender, receiver

def check_balance(user):
    return float(_round(user["balance"]))

def apply_interest(user, rate=0.015):
    balance = _round(user["balance"])
    interest = _round(balance * Decimal(rate))
    balance += interest
    user["balance"] = float(balance)

    user["transactions"].append(
        _new_transaction("interest", interest, balance, "system")
    )

    return user

def calculate_monthly_fees(user, fee_schedule):
    total_fee = Decimal("0.00")

    for fee in fee_schedule.values():
        total_fee += _round(fee)

    balance = _round(user["balance"])
    if balance - total_fee < MIN_BALANCE:
        raise ValueError("Fees exceed balance")

    balance -= total_fee
    user["balance"] = float(balance)

    user["transactions"].append(
        _new_transaction("fees", total_fee, balance, "system")
    )

    return user
