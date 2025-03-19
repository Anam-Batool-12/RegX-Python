import re

def validate(email):
    req = r"""
    ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$    
    """
    if re.match(req, email, re.VERBOSE):
        return True
    else:
        return False

while True:
    email = input("Enter Email: ")
    if validate(email):
        print("Valid Email")
        break
    else:
        print("Invalid Email")
    print("Do you want to continue? (Y/N)")
    ans = input()
    if ans.lower() == 'n':
        break
