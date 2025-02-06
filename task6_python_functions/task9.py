from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + [x[-1] + y] if x else [y], numbers, [])
print(total)