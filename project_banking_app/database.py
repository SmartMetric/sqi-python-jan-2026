import sqlite3
DB_NAME = "banking_app.db"
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL CHECK(trim(first_name) <> ''),
            last_name TEXT NOT NULL CHECK(trim(last_name) <> ''),
            email TEXT NOT NULL UNIQUE CHECK(trim(email) <> ''),
            phone_number TEXT NOT NULL UNIQUE CHECK(trim(phone_number) <> ''),
            username TEXT NOT NULL UNIQUE CHECK(trim(username) <> ''),
            password_hash TEXT NOT NULL CHECK(password_hash <> ''),
            account_number TEXT NOT NULL UNIQUE CHECK(account_number <> ''),
            balance INTEGER NOT NULL DEFAULT 0 CHECK(balance >= 0),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
conn = sqlite3.connect("banking_app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL CHECK(trim(first_name) <> ''),
    last_name TEXT NOT NULL CHECK(trim(last_name) <> ''),
    email TEXT NOT NULL UNIQUE CHECK(trim(email) <> ''),
    phone_number TEXT NOT NULL UNIQUE CHECK(trim(phone_number) <> ''),
    username TEXT NOT NULL UNIQUE CHECK(trim(username) <> ''),
    password_hash TEXT NOT NULL CHECK(password_hash <> ''),
    account_number TEXT NOT NULL UNIQUE CHECK(account_number <> ''),
    balance INTEGER NOT NULL DEFAULT 0 CHECK(balance >= 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
""")

