books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
for value in books.values():
    print(f'Book: {value["title"]}, Author:  {value["author"]}, Year: {value["year"]}')