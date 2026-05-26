import random


def generate_password(length, use_upper, use_lower, use_numbers):
    characters = ""

    if use_upper:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if use_numbers:
        characters += "0123456789"

    if characters == "":
        return "Error: You must choose at least one option!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("~~~ Password Generator ~~~")

    length = int(input("Enter password length: "))

    upper = input("Include uppercase? (yes/no): ").lower() == "yes"
    lower = input("Include lowercase? (yes/no): ").lower() == "yes"
    numbers = input("Include numbers? (yes/no): ").lower() == "yes"

    password = generate_password(length, upper, lower, numbers)

    print(f"\nGenerated Password: {password}")
    print(f"Password generated with {length} length")


if __name__ == "__main__":
    main()
