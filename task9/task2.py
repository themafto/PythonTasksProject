FILE_PATH = "sample.txt"

with open(FILE_PATH, mode = "w") as file:
    file.write("Hello world!")

with open(FILE_PATH, mode = "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(content, "\nWord count:", word_count)