"""1. Exercises"""
number = []

for i in range(5):
    user_number = int(input("Number: "))
    number.append(user_number)

print(f"The first number is: {number[0]}")
print(f"The last number is: {number[4]}")
print(f"The smallest number is: {min(number)}")
print(f"The largest number is: {max(number)}")
average = sum(number) / len(number)
print(f"The average of the numbers: {average}")


"""Security Checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_username = input("Please enter your username")
password_check = 0
if user_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
