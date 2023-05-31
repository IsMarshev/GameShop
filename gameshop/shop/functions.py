import hashlib
import random


def generated_salt():
    return hashlib.sha256(str(random.randint(1000000, 10000000)).encode(encoding='UTF-8', errors='strict')).hexdigest()


def hashing(password, salt):
    password += salt
    password = hashlib.sha256(password.encode(
        encoding='UTF-8', errors='strict')).hexdigest()
    return password


def check_password(salt, password, true_password):
    password = hashing(password, salt)
    if password == true_password:
        return True
