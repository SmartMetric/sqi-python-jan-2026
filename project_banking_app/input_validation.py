import re


def validate_name(name):
    if not name.strip():
        return False
    return name.isalpha()


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def validate_phone(phone):
    if not phone.isdigit():
        return False
    if len(phone) != 11:
        return False
    return True


def validate_username(username):
    if not username.strip():
        return False
    if len(username) < 4:
        return False
    return True


def validate_password(password):
    if len(password) < 6:
        return False
    return True