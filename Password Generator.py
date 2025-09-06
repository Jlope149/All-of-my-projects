import random
import string

def generate_password(length:int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation   # Puts every character in the ascii table together
    password = "".join(random.choice(alphabet) for i in range(length))     # puts random characters together by the set length
    return password

password = generate_password()
print(f"Generated Password: {password}")