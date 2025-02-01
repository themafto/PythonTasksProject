list_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print('First day: ' + list_of_days[0],'\nLast day: ' + list_of_days[-1])
print('Middle days: ', ', '.join(list_of_days[1:-1]))

list_of_days[2] = 'Humpday'
print('Updated list: ', list_of_days)
