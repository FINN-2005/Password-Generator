import secrets
import string

def generate_password(length=16, symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = "!@#$%^&*()-_=+[]{};:<>?,./"

    charset = letters + digits
    if symbols:
        charset += punctuation

    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password

# Example usage:
print(generate_password())
print(generate_password())
print(generate_password())
print(generate_password())
print(generate_password())