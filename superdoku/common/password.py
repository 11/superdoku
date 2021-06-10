import os
import bcrypt


def encrypt(pwd):
    salt = bcrypt.gensalt()
    pepper = os.environ.get('PEPPER')
    seasoned_pwd = str(pwd + pepper).encode()
    hash = bcrypt.hashpw(seasoned_pwd, salt)
    return salt, hash


def decrpyt(pwd, salt):
    pepper = os.environ.get('PEPPER')
    seasoned_pwd = str(pwd + pepper).encode()
    return bcrypt.hashpw(seasoned_pwd, salt)
