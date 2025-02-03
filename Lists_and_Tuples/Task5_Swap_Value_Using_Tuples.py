first_value = input("Enter a first value: ")
second_value = input("Enter a second value: ")
print(f'Before swap:  {first_value}, {second_value}')
first_value, second_value = second_value , first_value
print(f'After swap:  {first_value}, {second_value}')

