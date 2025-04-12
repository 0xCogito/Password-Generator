import random
import string

def get_user_input(prompt):
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("⚠️ Please enter 'y' or 'n'.")

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("❌ At least one character set must be selected!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n🔐 Welcome to the Password Generator!\n" + "-"*40)

    while True:
        try:
            length = int(input("🔢 Enter desired password length (e.g. 12): "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Please enter a valid positive number.")

    use_upper = get_user_input("Include uppercase letters?")
    use_lower = get_user_input("Include lowercase letters?")
    use_digits = get_user_input("Include numbers?")
    use_symbols = get_user_input("Include special characters?")

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n✅ Generated Password:\n", password)
    except ValueError as ve:
        print(ve)

    print("\n🎉 Thanks for using Password Generator!\n")

if __name__ == "__main__":
    main()
