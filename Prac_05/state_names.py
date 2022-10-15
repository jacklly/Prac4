"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# DONE: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

max_length_short = max(len(pair) for pair in CODE_TO_NAME)
max_length_long = max(len(CODE_TO_NAME[pair]) for pair in CODE_TO_NAME)

for pair in CODE_TO_NAME:
    print(f"{pair:{max_length_short}} is {CODE_TO_NAME[pair]:{max_length_long}}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:{max_length_short}} is {CODE_TO_NAME[state_code]:{max_length_long}}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
