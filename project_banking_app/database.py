import sqlite3

DB_NAME = "banking_app.db"

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = OFF")

    cursor.execute("DROP TABLE IF EXISTS cheques")
    cursor.execute("DROP TABLE IF EXISTS loans")
    cursor.execute("DROP TABLE IF EXISTS transfers")
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("DROP TABLE IF EXISTS accounts")
    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("PRAGMA foreign_keys = ON")

    # =====================================
    # 1. USERS TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL CHECK(trim(first_name) <> ''),
            last_name TEXT NOT NULL CHECK(trim(last_name) <> ''),
            email TEXT NOT NULL UNIQUE CHECK(trim(email) <> ''),
            phone_number TEXT NOT NULL UNIQUE CHECK(trim(phone_number) <> ''),
            username TEXT NOT NULL UNIQUE CHECK(trim(username) <> ''),
            password_hash TEXT NOT NULL CHECK(trim(password_hash) <> ''),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
    print("Users table ready.")

    # =====================================
    # 2. ACCOUNTS TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,

            account_number TEXT NOT NULL UNIQUE
                CHECK(account_number GLOB '475[0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),

            product_code INTEGER NOT NULL
                CHECK(product_code IN (1, 2, 3)),

            account_type TEXT NOT NULL
                CHECK(account_type IN ('savings', 'current', 'fixed')),

            balance REAL NOT NULL DEFAULT 0
                CHECK(balance >= 0),

            status TEXT NOT NULL DEFAULT 'active'
                CHECK(status IN ('active', 'closed', 'frozen')),

            last_withdrawal_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_interest_date TEXT DEFAULT CURRENT_TIMESTAMP,

            source_savings_account_id INTEGER,
            fixed_start_date TEXT,
            fixed_tenor_days INTEGER,
            fixed_maturity_date TEXT,
            fixed_locked INTEGER NOT NULL DEFAULT 0
                CHECK(fixed_locked IN (0, 1)),

            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            CHECK(
                (product_code = 1 AND account_type = 'savings') OR
                (product_code = 2 AND account_type = 'current') OR
                (product_code = 3 AND account_type = 'fixed')
            ),

            UNIQUE(user_id, product_code),

            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(source_savings_account_id) REFERENCES accounts(id)
        );
    """)
    print("Accounts table ready.")

    # =====================================
    # 3. TRANSACTIONS TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,

            transaction_type TEXT NOT NULL
                CHECK(transaction_type IN (
                    'deposit',
                    'withdrawal',
                    'interest',
                    'service_charge',
                    'fixed_funding',
                    'loan_repayment',
                    'cheque_withdrawal'
                )),

            amount REAL NOT NULL
                CHECK(amount > 0),

            reference TEXT NOT NULL UNIQUE
                CHECK(trim(reference) <> ''),

            description TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(account_id) REFERENCES accounts(id)
        );
    """)
    print("Transactions table ready.")

    # =====================================
    # 4. TRANSFERS TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE transfers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_account_id INTEGER NOT NULL,
            to_account_id INTEGER NOT NULL,

            amount REAL NOT NULL
                CHECK(amount > 0),

            reference TEXT NOT NULL UNIQUE
                CHECK(trim(reference) <> ''),

            narration TEXT,

            status TEXT NOT NULL DEFAULT 'completed'
                CHECK(status IN ('completed', 'failed', 'reversed')),

            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            CHECK(from_account_id <> to_account_id),

            FOREIGN KEY(from_account_id) REFERENCES accounts(id),
            FOREIGN KEY(to_account_id) REFERENCES accounts(id)
        );
    """)
    print("Transfers table ready.")

    # =====================================
    # 5. LOANS TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            linked_fixed_account_id INTEGER NOT NULL UNIQUE,

            loan_account_number TEXT NOT NULL UNIQUE
                CHECK(loan_account_number GLOB '475[0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),

            principal_amount REAL NOT NULL
                CHECK(principal_amount > 0),

            interest_rate REAL NOT NULL
                CHECK(interest_rate >= 0),

            amount_due REAL NOT NULL
                CHECK(amount_due >= 0),

            status TEXT NOT NULL DEFAULT 'active'
                CHECK(status IN ('active', 'paid', 'defaulted')),

            due_date TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(linked_fixed_account_id) REFERENCES accounts(id)
        );
    """)
    print("Loans table ready.")

    # =====================================
    # 6. CHEQUES TABLE
    # =====================================
    cursor.execute("""
        CREATE TABLE cheques (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,

            cheque_number TEXT NOT NULL UNIQUE
                CHECK(cheque_number GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][A-Z]'),

            cheque_serial INTEGER NOT NULL
                CHECK(cheque_serial > 0),

            status TEXT NOT NULL DEFAULT 'unused'
                CHECK(status IN ('unused', 'used', 'cancelled')),

            issued_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            used_at TEXT,

            FOREIGN KEY(account_id) REFERENCES accounts(id)
        );
    """)
    print("Cheques table ready.")

print("All tables created successfully.")