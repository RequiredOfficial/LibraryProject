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

     def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            if book.available:
                book.available = False
                print(f"Книга '{title}' выдана.")
            else:
                print(f"Книга '{title}' уже выдана.")
        else:
            print(f"Книга '{title}' не найдена.")
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            if not book.available:
                book.available = True
                print(f"Книга '{title}' возвращена.")
            else:
                print(f"Книга '{title}' уже в наличии.")
        else:
            print(f"Книга '{title}' не найдена.")
