def main():
    email = input("Email: ")
    mail_list = {}
    while email != "":
        predicted_name = name_predictor(email)
        choice = input(f"Is your name: {predicted_name} [Y/n]").upper()
        if choice == "Y" or "":
            name = predicted_name
        else:
            name = input("Please enter your name: ")
        mail_list[email] = name
        email = input("Next email: ")
    for pair in mail_list:
        print(f"{mail_list[pair]} ({pair})")


def name_predictor(email):
    predicted_name = email.split("@")[0]
    predicted_name = predicted_name.replace(".", " ")
    return predicted_name


main()
