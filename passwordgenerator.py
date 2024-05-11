import string
import random

def generate_password(length):

    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for _ in range(length))
    return password

def password_generated(length):
    result = generate_password(length)
    print("The generated password is:", result)

def main():
    length = int(input("Enter the length of the password to be generated: "))
    password_generated(length)

main()
