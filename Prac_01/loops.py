"""#1 Odd up to 20"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
print()

"""#2 Tens up to 100"""
for i in range(0, 110, 10):
    print(i, end=' ')
print()
print()

"""#3 Down from 20"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()
print()

"""#4 Stars"""
StarNo = int(input("How many stars would you like?"))
print("* " * StarNo)
print()
print()

"""#5 'n' Lines of increasing stars"""
LineNo = int(input("How many lines of (increasing) stars would you like?"))
stars = 0
while stars < LineNo:
    stars = stars + 1
    print("* " * stars)
