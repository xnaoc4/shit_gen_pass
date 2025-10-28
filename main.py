import secrets
import string

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

while True:
    try:
        user_length = int(input("Enter lentgh your password: "))
        if user_length <= 0:
            print(f"length {user_length} error")
            continue
        elif user_length <= 7 or user_length >= 128:
            print("error. 0xFF")
            continue
        else:
            print(f"Your password is: {gen_pass(user_length)}")
            break
    except ValueError:
        print("error. write the int number")