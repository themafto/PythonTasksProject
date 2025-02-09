class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"{self.title} by {self.author} \nYear_of_published: {self.year_published}"

book1 = Book("The Great Gatsby", "Scott Fitzgerald", 1999)
print(book1)