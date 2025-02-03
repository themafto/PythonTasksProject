phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
if "Alice" in phone_book:
    print('Alice number exist: ', phone_book["Alice"])
else:
    print('Alice number does not exist')
del phone_book["Bob"]

print(phone_book)