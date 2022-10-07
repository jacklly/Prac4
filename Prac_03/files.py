# 1.

def name_writer():
    out_file = open("name.txt", "w")
    name = input("What is your name?")
    print(name, file=out_file)
    out_file.close()


name_writer()


# 2.
def name_reader():
    in_file = open("name.txt", "r")
    name = in_file.read()
    print("Your name is: {}".format(name))
    in_file.close()



name_reader()
