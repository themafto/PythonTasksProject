import os
from datetime import datetime


file_name = "log.txt"
file_exists = os.path.exists(file_name)

with open("log.txt", mode = "a") as log:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"\nCurrent Date and Time: {current_time}\n")

    if file_exists:
        print(f"Appended: {current_time}")
    else:
        print(f"{file_name} created.\nAppended: {current_time}")

with open(file_name, mode = "r") as log:
    content = log.read()
    print("\nFile content:")
    print(content)

