menu = ("(H)ello \n(G)oodbye \n(Q)uit")

Name = input("Please enter your name:")

choice = 0

while choice != "Q":
    print(menu)
    choice = input("").upper()
    if choice == "H":
        print(f"Hello {Name}")
    elif choice == "G":
        print(f"Goodbye {Name}")
    elif choice == "Q":
        print("Finished")
        quit()
    else:
        print("Invalid Entry")