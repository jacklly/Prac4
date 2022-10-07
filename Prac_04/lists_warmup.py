numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0],
      numbers[-1],
      numbers[3],
      numbers[:-1],
      numbers[3:4],
      5 in numbers,
      7 in numbers,
      "3" in numbers,
      numbers + [6, 5, 3])
# 1
numbers[0] = 10
# 2
numbers[6] = 1
# 3
print(numbers[2: 7])
# 4
print(9 in numbers)
