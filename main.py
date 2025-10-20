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
        
