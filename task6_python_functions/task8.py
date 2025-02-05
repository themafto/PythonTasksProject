words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"
new_words = filter(lambda word: word.startswith(target_letter), words)
print(list(new_words))