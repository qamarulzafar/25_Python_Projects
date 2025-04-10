# password_generator_python_project


import random 
import string

print("Welcome to the password generator")
length = int(input('How long should your password be? '))


letters = string.ascii_letters
digits = string.digits
symbol = string.punctuation

all_char = letters + digits + symbol

password = ''.join(random.choice(all_char) for _ in range(length))
print(f"\n🧾 Your Generated Password: {password}")