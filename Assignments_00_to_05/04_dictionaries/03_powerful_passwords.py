
import hashlib

def hash_password(password):
    """Hashes a password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def login(email, password_to_check, stored_logins):
    """
    Verifies if the hash of the provided password matches the stored hash for the given email.

    Args:
        email (str): The email address to log in with.
        password_to_check (str): The password entered by the user.
        stored_logins (dict): A dictionary where keys are emails and values are their stored password hashes.

    Returns:
        bool: True if the password matches the stored hash, False otherwise.
    """
    if email in stored_logins:
        hashed_check = hash_password(password_to_check)
        if hashed_check == stored_logins[email]:
            return True
        else:
            return False
    else:
        return False

def main():
    """
    Demonstrates the login functionality with a sample stored logins dictionary.
    """
    stored_logins = {
        "user1@example.com": hash_password("securepassword123"),
        "another.user@test.org": hash_password("mysecret"),
        "guest@nowhere.net": hash_password("password")
    }

    print("Sample Logins (hashes):")
    for email, hashed_pw in stored_logins.items():
        print(f"{email}: {hashed_pw[:10]}...") # Print first 10 chars for brevity

    print("\nAttempting to log in user1@example.com...")
    if login("user1@example.com", "securepassword123", stored_logins):
        print("Login successful!")
    else:
        print("Login failed.")

    print("\nAttempting to log in user1@example.com with incorrect password...")
    if login("user1@example.com", "wrongpassword", stored_logins):
        print("Login successful!")
    else:
        print("Login failed.")

    print("\nAttempting to log in a non-existent user...")
    if login("nonexistent@user.com", "anypassword", stored_logins):
        print("Login successful!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()