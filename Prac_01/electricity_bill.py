print("Electricity bill estimator")

kWhPrice = int(input("Enter cents per kW:"))

DailyUse = int(input("Enter daily use in kW:"))
BillDays = int(input("Enter numer of billing days:"))

print(f"Estimated bill: ${kWhPrice * DailyUse * BillDays:.2f}")
print()
print()
print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = input("Which tariff? (11 or 31)")
if tariff == "11":
    tariff = TARIFF_11
elif tariff == "31":
    tariff = TARIFF_31
DailyUse = int(input("Enter daily use in kW:"))
BillDays = int(input("Enter numer of billing days:"))

print(f"Estimated bill: ${tariff * DailyUse * BillDays:.2f}")