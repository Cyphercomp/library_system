
from library_system.core import Book, Library
from library_system.utils import borrow_item

def main():
    library = Library(user_role="Admin")

    book_1 = Book("Mastering Object oriented python ", "Steven F. Lot", 992)
    book_2= Book("Python Object Oriented Programming", "Lott Phillips", 715)

    library.add_book(book_1)
    library.add_book(book_2)

    print("\nAll books:")
    for book in library:
        print(book, "- Pages:", len(book))

    print(f"\nBorrowing {book_1.title}")
    library.borrow_book(book_1)

    print(f"\nReturning {book_2.title}")
    library.return_book(book_2)

    print("\nDuck Typing Test:")

    class Magasine:
        def __init__(self, title):
            self.title = title

    magasine= Magasine("Python Direct")
    borrow_item(magasine)


if __name__ == "__main__":
    main()