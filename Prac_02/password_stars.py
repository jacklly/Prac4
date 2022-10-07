def main():
    """Password print"""
    password = "0"
    password = get_password(password)

    password_length = len(password)
    print("Your password is: ", password_length * "*")


def get_password(password):
    """Password checker"""
    password = input("What would you like to set your password as? (Min. 5 characters)")
    while len(password) < 5:
        print("Please enter a longer password!")
        password = input("What would you like to set your password as? (Min. 5 characters)")
    return password


main()
