list_of_integer = [10, 20, 30, 40, 50, 11, 17, 22]
summ = 0
count = 0
for i, value in enumerate(list_of_integer):
    if value % 2 == 0:
        summ += value
        count += 1

print(f'Sum of even numbers: {summ} \nNumber of even numbers: {count}')