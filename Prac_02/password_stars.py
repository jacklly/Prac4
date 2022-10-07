def main():
    """Password print"""
    Psw = "0"
    Psw = get_password(Psw)

    PswLen = len(Psw)
    print("Your password is: ", PswLen * "*")


def get_password(Psw):
    """Password checker"""
    Psw = input("What would you like to set your password as? (Min. 5 characters)")
    while len(Psw) < 5:
        print("Please enter a longer password!")
        Psw = input("What would you like to set your password as? (Min. 5 characters)")
    return Psw


main()
