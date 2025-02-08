import csv
from email.quoprimime import header_encode

file_name = "students.csv"

with open(file_name, mode = "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])

    writer.writerow(["Alice", 25, "A"])
    writer.writerow(["Bob", 22, "B"])
    writer.writerow(["Charlie", 24, "A"])

print(f"File {file_name} was created and filled.")

total_age = 0
count = 0

with open(file_name, mode = "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("\nFile contents:")
    print(", ".join(header))

    for row in reader:
        print(", ".join(row))
        total_age += int(row[1])
        count += 1
average_age = total_age / count
print(f"\nСредний возраст студентов: {average_age:.2f}")