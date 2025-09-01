import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    # base characters: a-z + A-Z
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # !@#$ etc.

    # agar user ne length chhoti di toh warning
    if length < 6:
        print("⚠️ Password length should be at least 6 for security.")
        length = 6

    # password generate
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# program start
print("🔐 Welcome to Advanced Password Generator 🔐")

try:
    length = int(input("👉 Enter password length (default 12): ") or 12)
except ValueError:
    print("Invalid input, using default length 12")
    length = 12

use_digits = input("Include digits? (y/n): ").lower() == "y"
use_special = input("Include special characters? (y/n): ").lower() == "y"

password = generate_password(length, use_digits, use_special)

print("\n✅ Your Secure Password is:", password)
