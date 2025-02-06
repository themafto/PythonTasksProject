def min_max_avg(numbers):
    if len(numbers) == 0:
        return "The list of numbers is empty"

    min_value = min(numbers)
    max_value = max(numbers)
    avg_value = sum(numbers) / len(numbers)
    return min_value, max_value, avg_value

numbers_list = [1, 2, 3, 4, 5]
min_value, max_value, avg_value = min_max_avg(numbers_list)
print(min_value, max_value, avg_value)