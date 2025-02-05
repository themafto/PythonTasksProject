names = ["Alice", "Bob", "Charlie"]
names_length = map(lambda x: (x, len(x)), names)
print(list(names_length))