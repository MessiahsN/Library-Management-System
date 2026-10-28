

class Book:
    # Contructor
    def __init__(self, title, author, isbn, is_available):
        self.title = str(title)
        self.author = str(author)
        self.isbn = str(isbn)
        self.is_available = bool(is_available)

    # Update book availablity
    def borrow_a_book(self):
        print(f"You have succesfully borrowed the - {self.title} book")
        self.is_available = False

    def return_a_book(self):
        print(f"You have succesfully returned the - {self.title} book")
        self.is_available = True

    def save_books_to_library():
        pass



book1 = Book("Lord of the rings", "William Shakespeare", "ISBN 5000 667255 76664", True)


# Book 2
book2 = Book("Oliver Twist", "Charles Dickens", "ISBN 6645 4343 8264", True)


book2.borrow_a_book()

book2.return_a_book()






