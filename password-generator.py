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

def generate_password(length:int, upper:bool=None, symbols:bool=None):
    combination = string.digits + string.ascii_lowercase
    
    

    if upper:
        print("upper +")
        combination += string.ascii_uppercase

    if symbols:
        print("symbols +")
        combination += string.punctuation

    c_len = len(combination)
    new_pass = ""

    for i in range(length):
        new_pass += combination[secrets.randbelow(c_len)]
    
    return new_pass

def pass_check(string):
    if upper_check(string):
        print("Password has upper case letters.")

    if lower_check(string):
        print("Password has lower case letters.")

    if symb_check(string):
        print("Password has special characters.")

    if digit_check(string):
        print("Password has numbers.")


def main():
    print("Choose one operation below:")
    print("1. Generate Password.")
    print("2. Password checker.")
    print()
    choice = int(input("Please enter your choice... "))

    if choice==1:
        print()
        l = int(input("Please enter the length of the password:"))
        print()
        u = input("Do you want uppercase [Y/N]: ").lower()
        s = input("Do you want special characters [Y/N]: ")
        print()

        if u=="y":
            u=True
        else:
            u=False
        
        if s=="y":
            s=True
        else:
            s=False

        new = generate_password(l, u, s)
        print(new)

    
    if choice==2:
        print()
        pwd = getpass.getpass(prompt="Enter Password:")
        print()
        pass_check(pwd)

if __name__=="__main__":
    main()