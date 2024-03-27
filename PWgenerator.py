import string
import random

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    """
    Generate a random password of specified length and complexity.

    Args:
    - length (int): Length of the password.
    - uppercase (bool): Include uppercase letters.
    - lowercase (bool): Include lowercase letters.
    - digits (bool): Include digits.
    - symbols (bool): Include symbols.

    Returns:
    - str: Randomly generated password.
    """
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def display_passwords(passwords):
    """
    Display generated passwords in a user-friendly format.

    Args:
    - passwords (list): List of generated passwords.
    """
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password}")

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            raise ValueError("Number of passwords must be a positive integer.")

        passwords = []
        for _ in range(num_passwords):
            length = int(input("Enter the length of the password: "))
            uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            digits = input("Include digits? (y/n): ").lower() == 'y'
            symbols = input("Include symbols? (y/n): ").lower() == 'y'
            password = generate_password(length, uppercase, lowercase, digits, symbols)
            passwords.append(password)

        display_passwords(passwords)

        # Option to copy password to clipboard
        copy_to_clipboard = input("Do you want to copy any of these passwords to clipboard? (y/n): ").lower() == 'y'
        if copy_to_clipboard:
            index = int(input("Enter the index of the password to copy: ")) - 1
            if 0 <= index < len(passwords):
                print("Password copied to clipboard.")
            else:
                print("INVALID INDEX.")

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
