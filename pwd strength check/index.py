import re
def check_pwd(pwd):
    length = r".{8,}"
    lower = r"[a-z]"
    upper = r"[A-Z]"
    digit = r"[0-9]"
    special = r"[!@#$%^&*()]"

    if not re.search(length, pwd):
        return " Password must be at least 8 characters long.", False
    if not re.search(lower, pwd):
        return " Password must contain at least one lowercase letter.", False
    if not re.search(upper, pwd):
        return " Password must contain at least one uppercase letter.", False
    if not re.search(digit, pwd):
        return " Password must contain at least one digit.", False
    if not re.search(special, pwd):
        return " Password must contain at least one special character.", False

    return "Password is strong!", True

while True:
    print("\n Password Strength Checker ")
    print("1. Check password strength")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "2":
        print("Goodbye!")
        break
    elif choice == "1":
        pwd = input("Enter password to check: ")
        message, is_strong = check_pwd(pwd)
        print(message)
        if is_strong:
            print("Exiting program as password is strong.")
            break
    else:
        print("⚠Invalid choice. Please try again.")
