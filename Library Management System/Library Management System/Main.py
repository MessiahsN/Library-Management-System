import re


class Book:
    def __init__(self, title, author, isbn):
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN cannot be empty.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Default availability status

    def update_availability(self, status):
        """Updates availability status to True (Available) or False (Checked Out)."""
        self.is_available = status

    def __str__(self):
        status_text = "Available" if self.is_available else "Checked Out"
        return f"[ISBN: {self.isbn}] '{self.title}' by {self.author} | Status: {status_text}"


# Task 1: Member Class with Email Validation
class Member:
    def __init__(self, name, email):
        if not name:
            raise ValueError("Member name cannot be empty.")
        
        self.name = name
        self.email = self.validate_email(email)
        self.borrowed_books = []  # Collection storing borrowed Book objects

    def validate_email(self, email):
        """Validates email format using Regular Expressions (Regex)."""
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(email_pattern, email):
            raise ValueError(f"'{email}' is not a valid email address format.")
        return email

    def __str__(self):
        return f"Member: {self.name} ({self.email}) | Borrowed Books: {len(self.borrowed_books)}"


# Core Operations
class Library:
    def __init__(self):
        # lists to store books and members
        self.books = []
        self.members = []

    def add_book(self, book):
        # 'self.books' is a list of all Book objects.
        # This loop inspects each book one by one to ensure the ISBN isn't duplicated.
        for existing_book in self.books:
            if existing_book.isbn.lower() == book.isbn.lower():
                raise ValueError("A book with this ISBN already exists.")
        self.books.append(book)

    def register_member(self, member):
        for existing_member in self.members:
            if existing_member.email.lower() == member.email.lower():
                raise ValueError("A member with this email is already registered.")
        self.members.append(member)

    def display_books(self):
        if not self.books:
            print("No books registered in the system.")
            return

        print("\n--- Book Catalog ---")
        # print each individual Book object
        for book in self.books:
            print(book)

    def display_members(self):
        if not self.members:
            print("No members registered in the system.")
            return

        print("\n--- Registered Members ---")
        for member in self.members:
            print(member)


    def search_books(self, search_term):
        results = []
        clean_query = search_term.strip().lower()

        # If query appears in title OR author, append the book to results.
        for book in self.books:
            title_match = clean_query in book.title.lower()
            author_match = clean_query in book.author.lower()

            if title_match or author_match:
                results.append(book)

        return results

    # Book Checkout & Assertions
    def checkout_book(self, isbn, member_email):
        found_book = None
        found_member = None

        # Search for target book in the system
        for book in self.books:
            if book.isbn.lower() == isbn.lower():
                found_book = book
                break  # Stop searching as soon as we find a match

        if not found_book:
            raise KeyError(f"Book with ISBN '{isbn}' was not found.")

        if not found_book.is_available:
            raise ValueError(f"The book '{found_book.title}' is currently checked out.")

        # Search for target member in the system
        for member in self.members:
            if member.email.lower() == member_email.lower():
                found_member = member
                break

        if not found_member:
            raise KeyError(f"Member with email '{member_email}' was not found.")

        # Execute checkout logic
        found_book.update_availability(False)
        found_member.borrowed_books.append(found_book)

        # Help with Assertion verifying program state post-checkout
        assert found_book.is_available is False, "Assertion Failed: Book state should be False after checkout."

    # Return Book System
    def return_book(self, isbn, member_email):
        found_member = None

        # Find member by email
        for member in self.members:
            if member.email.lower() == member_email.lower():
                found_member = member
                break

        if not found_member:
            raise KeyError(f"Member with email '{member_email}' was not found.")

        found_book = None
        # Search specifically inside the member's list of borrowed books
        for book in found_member.borrowed_books:
            if book.isbn.lower() == isbn.lower():
                found_book = book
                break

        if not found_book:
            raise KeyError(f"Book with ISBN '{isbn}' is not listed under this member's borrowed books.")

        # Execute return logic
        found_book.update_availability(True)
        found_member.borrowed_books.remove(found_book)

        # Assertion verifying program state post-return
        assert found_book.is_available is True, "Assertion Failed: Book state should be True after return."


# Interactive Console Interface
def main():
    library = Library()

    while True:
        print("\n===================================")
        print("    LIBRARY MANAGEMENT SYSTEM      ")
        print("===================================")
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Register New Member")
        print("4. Display All Members")
        print("5. Search Books (Title or Author)")
        print("6. Check Out Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("\nSelect an option (1-8): ").strip()

        try:
            if choice == "1":
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                library.add_book(Book(title, author, isbn))
                print("Success: Book added.")

            elif choice == "2":
                library.display_books()

            elif choice == "3":
                name = input("Enter Member Name: ")
                email = input("Enter Member Email: ")
                library.register_member(Member(name, email))
                print("Success: Member registered.")

            elif choice == "4":
                library.display_members()

            elif choice == "5":
                query = input("Enter title or author: ")
                results = library.search_books(query)
                print(f"\n--- Search Results ({len(results)}) ---")
                for book in results:
                    print(book)

            elif choice == "6":
                isbn = input("Enter Book ISBN to Check Out: ")
                email = input("Enter Member Email: ")
                library.checkout_book(isbn, email)
                print("Success: Book checked out.")

            elif choice == "7":
                isbn = input("Enter Book ISBN to Return: ")
                email = input("Enter Member Email: ")
                library.return_book(isbn, email)
                print("Success: Book returned.")

            elif choice == "8":
                print("Exiting application...")
                break
            else:
                print("Invalid entry. Please select a number from 1 to 8.")

        except ValueError as ve:
            print(f"Validation Error: {ve}")
        except KeyError as ke:
            print(f"Lookup Error: {ke}")
        except AssertionError as ae:
            print(f"Assertion Failure: {ae}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()