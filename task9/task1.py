#with open("my_file") as file:
#    contents = file.read()
#    print(contents)

# with open("my_file", mode = "a") as file:
#     file.write("New Texts.")


with open("user_info.txt", mode = "a") as file:
    name = input("Your name: ")
    age = input("Your age: ")
    color = input("Your favorite color: ")

    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Favorite Color: {color}\n")