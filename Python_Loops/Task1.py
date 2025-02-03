list_of_integer = [3, 7, 1, 9, 4, 17, 122, 12]
for i in range(len(list_of_integer)):
    list_of_integer[i] *= 3
    if list_of_integer[i] > 15:
        list_of_integer[i] = 'Too large'

print(f'Modified list: {list_of_integer}')
