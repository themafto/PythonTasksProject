numbers = [-3, 5, 0, -1, 8, 2]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        numbers[i] = 0
    elif numbers[i] > 0:
        numbers[i] *= 2
    else:
        pass
    i +=1
print(numbers)


