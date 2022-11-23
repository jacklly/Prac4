"""
Taxi Sim
Jack Kelly
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "Limo", 2), SilverServiceTaxi(200, "Hummer", 4)]
    bill_value = 0
    choice = None
    taxi_choice = None
    print("Let's drive!")
    while choice != "q":
        choice = choice_getter()
        if choice == "c":
            print("Taxis available:")
            taxi_print(taxis)
            pass_value = True
            while pass_value:
                choice = int(input("Taxi choice:"))
                try:
                    taxi_choice = taxis[choice]
                    pass_value = False
                except IndexError:
                    print("Invalid taxi choice")
            print(f"Bill to date: ${bill_value:.2f}")

        elif choice == "d":
            if not taxi_choice:
                print("You need to choose a taxi before you can drive")
            else:
                taxi_choice.start_fare()
                distance = int(input("Drive how far? "))
                taxi_choice.drive(distance)
                print(f"Your {taxi_choice.name} trip cost you ${taxi_choice.get_fare():.2f}")
                bill_value += taxi_choice.get_fare()
            print(f"Bill to date: ${bill_value:.2f}")

        else:
            print("Invalid option")
    print(f"Total trip cost: ${bill_value:.2f}\nTaxis are now:")
    taxi_print(taxis)


def taxi_print(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choice_getter():
    choice = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    return choice


main()
