my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

new_set = {num**2 for num in my_set if num % 2 == 0}
print(new_set)