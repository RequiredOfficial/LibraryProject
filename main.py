from library import Library

def validate_isbn(isbn):
    return len(isbn.strip()) > 0 and isbn.replace("-", "").isdigit()

def get_valid_isbn():
    while True:
        isbn = input("ISBN: ").strip()
        if validate_isbn(isbn):
            return isbn
        print("Ошибка: ISBN должен содержать только цифры и дефисы.")
        
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

        elif choice == "4":
            title = input("Введите название книги для выдачи: ").strip()
            library.borrow_book(title)
        
        elif choice == "5":
            title = input("Введите название книги для возврата: ").strip()
            library.return_book(title)
        
        elif choice == "6":
            title = input("Введите название книги для удаления: ").strip()
            library.remove_book(title)
        
        elif choice == "7":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
