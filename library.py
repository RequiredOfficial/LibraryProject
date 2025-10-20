from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Книга '{title}' добавлена.")
    
    def remove_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                print(f"Книга '{title}' удалена.")
                return
        print(f"Книга с названием '{title}' не найдена.")
    
    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(book)
