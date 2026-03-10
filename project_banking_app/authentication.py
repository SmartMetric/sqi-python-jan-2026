import sqlite3
from toolbox import hash_password, generate_unique_account_number
from input_validation import (
    validate_name,
    validate_email,
    validate_phone,
    validate_username,
    validate_password
)

DB_NAME = "banking_app.db"


def register_user():
    print("\n--- User Registration ---")

    first_name = input("Enter first name: ").strip()
    if not validate_name(first_name):
        print("Invalid first name")
        return

    last_name = input("Enter last name: ").strip()
    if not validate_name(last_name):
        print("Invalid last name")
        return

    email = input("Enter email: ").strip()
    if not validate_email(email):
        print("Invalid email")
        return

    phone = input("Enter phone number: ").strip()
    if not validate_phone(phone):
        print("Invalid phone number")
        return

    username = input("Enter username: ").strip()
    if not validate_username(username):
        print("Invalid username")
        return

    password = input("Enter password: ").strip()
    if not validate_password(password):
        print("Password must be at least 6 characters")
        return

    password_hash = hash_password(password)
    account_number = generate_unique_account_number()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id
            FROM users
            WHERE email = ? OR phone_number = ? OR username = ?
        """, (email, phone, username))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Email, phone number, or username already exists")
            return

        cursor.execute("""
            INSERT INTO users (
                first_name,
                last_name,
                email,
                phone_number,
                username,
                password_hash
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, username, password_hash))

        user_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO accounts (
                user_id,
                account_number,
                product_code,
                account_type,
                balance
            )
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, account_number, 1, "savings", 0))

    print("\nRegistration successful!")
    print(f"Your default savings account number is: {account_number}")


def login_user():
    print("\n--- User Login ---")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    password_hash = hash_password(password)

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, first_name, last_name, username
            FROM users
            WHERE username = ? AND password_hash = ?
        """, (username, password_hash))
        user = cursor.fetchone()

    if not user:
        print("Invalid username or password")
        return None

    print(f"\nWelcome, {user[1]} {user[2]}!")
    return user


def get_user_by_id(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, first_name, last_name, email, phone_number, username, created_at
            FROM users
            WHERE id = ?
        """, (user_id,))
        return cursor.fetchone()


def get_user_accounts(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, account_number, product_code, account_type, balance, status, created_at
            FROM accounts
            WHERE user_id = ?
            ORDER BY product_code
        """, (user_id,))
        return cursor.fetchall()


def user_has_account_type(user_id, account_type):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id
            FROM accounts
            WHERE user_id = ? AND account_type = ?
        """, (user_id, account_type))
        account = cursor.fetchone()

    return account is not None


def open_current_account(user_id):
    if user_has_account_type(user_id, "current"):
        print("You already have a current account")
        return

    account_number = generate_unique_account_number()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO accounts (
                user_id,
                account_number,
                product_code,
                account_type,
                balance
            )
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, account_number, 2, "current", 0))

    print("Current account opened successfully")
    print(f"Your current account number is: {account_number}")


def show_user_accounts(user_id):
    accounts = get_user_accounts(user_id)

    if not accounts:
        print("No account found")
        return

    print("\n--- My Accounts ---")
    for account in accounts:
        print(f"Account Number: {account[1]}")
        print(f"Account Type: {account[3]}")
        print(f"Balance: {account[4]}")
        print(f"Status: {account[5]}")
        print("-" * 30)