import string
import random

# Get all letters (both uppercase and lowercase) and digits
random_character = string.ascii_letters + string.digits

# Get input from the user for the length of the password
specified_length = int(input("Enter your password length: "))

# Generate a random password of the specified length
password = ''.join(random.choice(random_character) for _ in range(specified_length))

print("The generated password is:", password)
