from file_manager import load_users_from_file, save_users_to_file
from user import register_user, login_user
from bank_operations import (
    deposit_money,
    withdraw_money,
    transfer_funds,
    check_balance
)
from report import view_transaction_history

USERS_FILE = "data/users.json"


def user_menu(users, current_user):
    while True:
        print(f"\nWelcome, {current_user['username']}")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transactions")
        print("6. Logout")

        choice = input("Choose: ")

        try:
            if choice == "1":
                print("Balance:", check_balance(current_user))

            elif choice == "2":
                amount = float(input("Amount to deposit: "))
                deposit_money(current_user, amount)
                save_users_to_file(USERS_FILE, users)
                print("Deposit successful")

            elif choice == "3":
                amount = float(input("Amount to withdraw: "))
                withdraw_money(current_user, amount)
                save_users_to_file(USERS_FILE, users)
                print("Withdrawal successful")

            elif choice == "4":
                receiver = input("Send to username: ")
                amount = float(input("Amount to transfer: "))
                transfer_funds(users, current_user["username"], receiver, amount)
                save_users_to_file(USERS_FILE, users)
                print("Transfer successful")

            elif choice == "5":
                transactions = view_transaction_history(current_user)

                if not transactions:
                    print("No transactions yet.")
                else:
                    print("\n--- Transaction History ---")
                    for t in transactions:
                        print(
                            f"{t['timestamp']} | {t['type']} | "
                            f"Amount: {t['amount']} | Balance: {t['balance_after']}"
                        )

            elif choice == "6":
                print("Logged out")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


def main():
    users = load_users_from_file(USERS_FILE)

    while True:
        print("\n=== Banking System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                register_user(users, username, password)
                save_users_to_file(USERS_FILE, users)
                print("Registration successful")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            user = login_user(users, username, password)
            if user:
                user_menu(users, user)
            else:
                print("Login failed")

        elif choice == "3":
            save_users_to_file(USERS_FILE, users)
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()




