import random


def choiceengine():
    choice = str(input(" (G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit\n ").upper())
    return (choice)


def score_returner(score):
    if score > 100 or score < 0:
        print("Invalid score\n ")
    elif score >= 90:
        print("Excellent score\n ")
    elif score >= 50:
        print("Passable score\n ")
    else:
        print("Bad score\n ")


def random_scorer2():
    score = random.randint(0, 100)
    return score


def main():
    score = -1
    choice = choiceengine()
    while choice != 'Q':
        if choice == 'G':
            score = random_scorer2()
            print("Your score is: {}\n ".format(score))
            choice = choiceengine()
        elif choice == 'P':
            if score == -1:
                print("Please get a valid score first!\n ")
                choice = choiceengine()
            else:
                print("Your score is: {}\n ".format(score))
                score_returner(score)
                choice = choiceengine()
        elif choice == 'S':
            if score == -1:
                print("Please get a valid score first!\n ")
                choice = choiceengine()
            else:
                print(score * "*")
                choice = choiceengine()


main()

print("Thank you for using this function!")
