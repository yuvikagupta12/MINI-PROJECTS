import random
import string

# Custom Exception
class WeakPasswordError(Exception):
    pass

# Function to generate strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to validate password
def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        raise WeakPasswordError("Password must contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain at least one digit.")

    if not any(char in string.punctuation for char in password):
        raise WeakPasswordError("Password must contain at least one special character.")

    return True

# Main Program
print("Generated Strong Password:", generate_password())

user_password = input("\nEnter a password to validate: ")

try:
    if validate_password(user_password):
        print("Password is Strong and Valid!")

except WeakPasswordError as e:
    print("Invalid Password:", e)