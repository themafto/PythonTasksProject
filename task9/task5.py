import csv

file_name = "employees.csv"

with open(file_name, mode = "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Position", "Salary"])

    writer.writerow(["John", "Manager", 5000])
    writer.writerow(["Alice", "Developer", 4000])
    writer.writerow(["Bob", "Designer", 3500])
print(f"File {file_name} created!!!")

total_salary = 0
count = 0

with open(file_name, mode = "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("\nFile contents:")
    print(", ".join(header))

    for row in reader:
        print(", ".join(row))
        total_salary += int(row[2])
        count += 1

average_salary = total_salary / count

print(f"\nAVG salary: {average_salary:.2f}")



