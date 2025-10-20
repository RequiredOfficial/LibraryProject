class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "В наличии" if self.available else "Выдана"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
