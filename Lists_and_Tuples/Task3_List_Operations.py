list_of_integers = [5, 12, 7, 9, 20, 15]

list_of_integers.append(25)
print(f'After adding 25: {list_of_integers}')

list_of_integers.remove(7)
print(f'After deleting 25: {list_of_integers}')

list_of_integers.sort()
print(f'After sorting {list_of_integers}')

print('Largest number: ' + str(max(list_of_integers)))
print('Minimum number: ' + str(min(list_of_integers)))
