"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month_value in range(1, number_of_months + 1):
        income = float(input(f" Enter income for month {month_value}: "))
        incomes.append(income)

    report_print(incomes, number_of_months)


def report_print(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month_value in range(1, number_of_months + 1):
        income = incomes[month_value - 1]
        total += income
        print(f"Month {month_value:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
