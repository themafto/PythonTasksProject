while True:
    number = int(input("Enter a number: "))
    if 0 < number < 10:
        print(f'Thank you! Your number is {number}')
        break
    print("Invalid input. Try again.")
