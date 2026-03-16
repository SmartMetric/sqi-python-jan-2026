import random
import string
import hashlib
import sqlite3
from datetime import datetime

DB_NAME = "banking_app.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_account_number():
    return "475" + "".join(random.choices(string.digits, k=7))


def generate_unique_account_number():
    while True:
        account_number = generate_account_number()

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM accounts WHERE account_number = ?",
                (account_number,)
            )
            existing_account = cursor.fetchone()

        if not existing_account:
            return account_number


def generate_transaction_reference():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_part = "".join(random.choices(string.digits, k=4))
    return f"TXN{timestamp}{random_part}"


def generate_unique_transaction_reference():
    while True:
        reference = generate_transaction_reference()

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM transactions WHERE reference = ?",
                (reference,)
            )
            existing_reference = cursor.fetchone()

        if not existing_reference:
            return reference


def generate_transfer_reference():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_part = "".join(random.choices(string.digits, k=4))
    return f"TRF{timestamp}{random_part}"


def generate_unique_transfer_reference():
    while True:
        reference = generate_transfer_reference()

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM transfers WHERE reference = ?",
                (reference,)
            )
            existing_reference = cursor.fetchone()

        if not existing_reference:
            return reference


def generate_loan_account_number():
    while True:
        loan_account_number = generate_account_number()

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM loans WHERE loan_account_number = ?",
                (loan_account_number,)
            )
            existing_loan = cursor.fetchone()

        if not existing_loan:
            return loan_account_number


def generate_cheque_number(account_number, cheque_serial):
    account_fragment = account_number[-4:]
    serial_part = str(cheque_serial).zfill(5)
    random_letter = random.choice(string.ascii_uppercase)
    return f"{account_fragment}{serial_part}{random_letter}"


def generate_unique_cheque_number(account_number, cheque_serial):
    while True:
        cheque_number = generate_cheque_number(account_number, cheque_serial)

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM cheques WHERE cheque_number = ?",
                (cheque_number,)
            )
            existing_cheque = cursor.fetchone()

        if not existing_cheque:
            return cheque_number