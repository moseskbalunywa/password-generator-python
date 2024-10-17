import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Create a pool of characters to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    # Combine all characters into one pool
    all_characters = lower + upper + digits + special

    if not all_characters:
        raise ValueError("At least one character type must be selected")

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    print("Password Generator started")  # Add this line to confirm script execution
    try:
        password_length = int(input("Enter password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(password_length, include_uppercase, include_numbers, include_special)
        print(f"Generated password: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")  # Add error handling
