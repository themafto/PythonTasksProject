user_year_number = int(input("Enter a year number: "))
if (user_year_number % 4 == 0 and user_year_number % 100 != 0) or user_year_number % 400 == 0:
    print(f"The year {user_year_number} is a leap year.")
else:
    print(f"The year {user_year_number} is not a leap year.")