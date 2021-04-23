import os
# import hashlib
import bcrypt

"""
TODO : 
    add a PATH 
    transfer the password string from the password generator
"""

password = b'HelloWorld'


def hash_password (password : str) -> str :
    return bcrypt.hashpw(password, bcrypt.gensalt())


def store_in_file (password : str) : 
    file = open('password.txt', "w")
    file.write(hash_password(password))
    file.close()


