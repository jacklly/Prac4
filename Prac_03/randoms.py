import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1: 10, 7 (smallest No. could have been 5, largest could have been 19
2: 7, 3 (smallest is 3, largest 9)
3: 4.175182314127672, 4.6816109832275 (smallest 2.5, largest 5.4999999999999)
"""