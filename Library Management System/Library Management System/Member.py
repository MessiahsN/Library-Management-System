import re

# Regular expression for an email
# r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'



class Member:
    # Declare your constructor
    def __init__(self, name, email, books_borrowed = []):
        self.name = str(name)
        self.email = str(email)
        self.books_borrowed = books_borrowed



user_name = input("Please enter your name: ")
email = input("Please enter your email: ")
user_books_borrowed = []


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


if re.match(pattern, email):
    Member1 = Member(user_name, email, [] )
else:
    print("This email address is not a valid email address!")

        
