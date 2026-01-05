from bank_operations import deposit_money, withdraw_money

def test_deposit_money():
    user = {
        "balance": 100.0,
        "transactions": []
    }

    deposit_money(user, 50)
    assert user["balance"] == 150.0


def test_withdraw_money():
    user = {
        "balance": 100.0,
        "transactions": []
    }

    withdraw_money(user, 40)
    assert user["balance"] == 60.0

#Basic tests
