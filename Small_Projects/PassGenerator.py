import secrets
import string

def crear_password(longitud):
    Carac = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(longitud):
        password += secrets.choice(Carac)
    return password

NewPass = crear_password(20)
print(NewPass)