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

# 3.
"""add 1st number to second"""


def number_adder():
    with open("numbers.txt", "r") as in_file:
        text = in_file.readlines()
        solution = int(text[0]) + int(text[1])
        in_file.close()
        print(solution)


number_adder()


# 4
def all_numbers_adder():
    with open("numbers.txt", "r") as in_file:
        text = in_file.readlines()
        i = 0
        sum = 0
        for i in range(0, len(text)):
            sum = sum + int(text[i])
            i = i + 1
        in_file.close()
        print(sum)


all_numbers_adder()
