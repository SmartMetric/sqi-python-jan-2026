from authentication import (
    register_user,
    login_user,
    show_user_accounts,
    open_current_account
)
from transactions import deposit


def user_dashboard(user):
    while True:
        print("\n=== USER DASHBOARD ===")
        print("1. View My Accounts")
        print("2. Open Current Account")
        print("3. Deposit")
        print("4. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_user_accounts(user[0])

        elif choice == "2":
            open_current_account(user[0])

        elif choice == "3":
            deposit(user[0])

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid option")


def main():
    while True:
        print("\n=== BANKING APP ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            user = login_user()
            if user:
                user_dashboard(user)

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option")


main()