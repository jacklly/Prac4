colours = {"absolutezero": "#0048ba", "chestnut": "#954535", "darklavendar": "#734f96", "ferrarired": "#ff2800",
           "jazzberryjam": "#a50b5e", "pinkflamingo": "#fc74fd", "vanillaice": "#f38fa9", "zomp": "#39a78e",
           "egyptianblue": "#1034a6", "byzantine": "#bd33a4"}

open_message = "Colour choices are:"

print(open_message)
number = 1
for colour in colours:
    print(f"{number:3}. {colour}")
    number = number + 1


def colour_displayer():
    colour_choice = input("Please choose a colour name to reveal its code, or leave blank to exit.\nEntry: ").lower()
    while colour_choice != "":
        try:
            print(f"{colour_choice} has the colour code: {colours[colour_choice]}")
        except KeyError:
            print(f"Please enter a valid colour name!")
        colour_choice = input("Please choose a colour, or leave blank to exit.\nEntry: ").lower()


colour_displayer()
print("Thank you!")