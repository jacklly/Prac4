import random


def score_returner(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent score.")
    elif score >= 50:
        print("Passable score")
    else:
        print("Bad score")


def random_scorer():
    score = random.randint(1, 99)
    print("The random score was: ", score)
    score_returner(score)


def defined_scorer():
    score = int(input("What was your score? (1-99)"))
    while score < 1 or score > 99:
        print("Invalid input")
        score = int(input("What was your score?"))
    score_returner(score)


random_scorer()

defined_scorer()
