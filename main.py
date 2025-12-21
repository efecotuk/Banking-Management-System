from file_manager import load_users_from_file, save_users_to_file
from user import register_user, login_user

USERS_FILE = "data/users.json"

def main():
    users = load_users_from_file(USERS_FILE)

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            try:
                register_user(users, u, p)
                save_users_to_file(USERS_FILE, users)
                print("Registered successfully")
            except ValueError as e:
                print(e)

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            user = login_user(users, u, p)
            print("Login success" if user else "Login failed")

        elif choice == "3":
            save_users_to_file(USERS_FILE, users)
            break

if __name__ == "__main__":
    main()
