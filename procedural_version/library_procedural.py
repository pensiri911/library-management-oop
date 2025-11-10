# Test
class Book():
    def __init__(self,book_id, title, author, available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = available_copies
        self.available_copies = available_copies
    
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

class Member():
    def __init__(self,member_id, name, email):
        self.name = name
        self.id = member_id
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book.return_book:
            self.borrowed_books.pop(book)
            return True
        return False
    
    
class Library():
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book_id, title, author, available_copies):
        book = self.find_book(book_id)
        if book != None:
            return
        self.books.append(Book(book_id, title, author, available_copies))
        print(f"Book '{title}' added successfully!")
        
    def add_member(self, member_id, name, email):
        member = self.find_member(member_id)
        if member != None:
            return
        self.members.append(Member(member_id, name, email))
        print(f"Member '{name}' registered successfully!")
        
    def borrow(self, member_id, book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book == None:
            pass
        if member == None:
            pass
        if member.borrow_book(book):
            pass
        else:
            pass
        
    def return_book(self, member_id, book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book == None:
            pass
        if member == None:
            pass
        if member.return_book(book):
            pass
        else:
            pass
        
    def find_book(self, book_id):
        """Find a book by ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.id == member_id:
                return member
        return None
    
    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")
                
    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member} ===")
        if not member['borrowed_books']:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book['title']} by {book['author']}")