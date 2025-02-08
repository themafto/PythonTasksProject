with open("sample.txt", mode = "w") as file:
    file.write("Hello world!")

with open("sample.txt", mode = "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(content, "\nWord count:", word_count)