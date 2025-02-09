list_of_lists = [[1, 2, 3], [4, 5], [6, 7]]

new_list = [item for sublist in list_of_lists for item in sublist]
print(new_list)

