import bcrypt


def hash_password(password: str) -> str:
    """
    Hashes a given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def compare_passwords(password: str, hashed_password: str) -> bool:
    """
    Compares a given password with a hashed password.

    Args:
        password: The password to check.
        hashed_password: The hashed password to compare with.

    Returns:
        True if the passwords match, False otherwise.
    """

    hashed_password_bytes = hashed_password.encode('utf-8')
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
