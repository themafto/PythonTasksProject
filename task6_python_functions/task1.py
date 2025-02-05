def format_name(name, title = "Mr./Ms."):
    if " " in name:
        first_name = name.split(" ")[0]
    else:
        first_name = name

    return f"Title: {title}, Name: {first_name}"

print(format_name("Alice Johnson"))