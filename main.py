def main():
    library = Library()
    
    while True:
        print("\n=== Библиотечная система ===")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Найти книгу")
        print("4. Взять книгу")
        print("5. Вернуть книгу")
        print("6. Удалить книгу")
        print("7. Выйти")
        
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            library.list_books()
        
        elif choice == "2":
            title = input("Название книги: ").strip()
            while not title:
                print("Название не может быть пустым.")
                title = input("Название книги: ").strip()
            
            author = input("Автор: ").strip()
            while not author:
                print("Автор не может быть пустым.")
                author = input("Автор: ").strip()
            
            isbn = get_valid_isbn()
            library.add_book(title, author, isbn)
        
        elif choice == "3":
            title = input("Введите название книги для поиска: ").strip()
            book = library.find_book(title)
            if book:
                print("Найдена книга:", book)
            else:
                print("Книга не найдена.")


        

