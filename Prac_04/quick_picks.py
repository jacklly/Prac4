import random

def main():
    number_of_lines = int(input("How many lines of random numbers would you like?"))
    while number_of_lines <= 0:
        print("Please try again!")
        number_of_lines = int(input("How many lines of random numbers would you like?"))

    for i in range(number_of_lines):
        number_list = []


        for x in range(6):
            random_number = random.randint(1, 45)
            number_list.append(random_number)

        number_list.sort()
        print(number_list)

main()