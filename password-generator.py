import string
import secrets
import re
import getpass

def upper_check(password):
    for item in password:
        if item.isupper():
            return True
    return False

def lower_check(password):
    for item in password:
        if item.islower():
            return True
    return False

def digit_check(password):
    for item in password:
        if item.isdigit():
            return True
    return False

def symb_check(password):   
    for item in password:
        if item in string.punctuation:
            return True
    return False

def generate_password(length:int, lower:bool=True, upper:bool=None, numbers:bool=True, symbols:bool=None):
    combination: str=string.ascii_lowercase + string.digits
    
    

    if upper:
        combination += string.ascii_uppercase

    if numbers:
        combination += string.digits

    if symbols:
        combination += string.punctuation

pwd = getpass.getpass("Password:")

print(upper_check(pwd))
