# Test
class Book():
    def __init__(self,book_id, title, author, available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
    
    def borrow_book(self):
        self.available_copies -= 1
        
    def return_book(self):
        self.available_copies += 1


class Member():
    def __init__(self,member_id, name, email):
        self.name = name
        self.id = member_id
        self.email = email
        self.borrowed_books = []

    def borrow(self, book_id):
        self.borrowed_books.append(book_id)
    
    
class Library():
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []
    
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
        if member == None:
            print("Error: Member not found!")
            return False
        if book == None:
            print("Error: Book not found!")
            return False
        if book.available_copies == 0:
            print("Error: No copies available!")
            return False
        if len(member.borrowed_books) == 3:
            print("Error: Member has reached borrowing limit!")
            return False
        book.borrow_book()
        member.borrow(book.id)
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member.name,
            'book_title': book.title
        }
        self.borrowed_books.append(transaction)
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        
        if book == None or member == None:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        book.return_book()
        member.borrowed_books.remove(book_id)
        
        for i, transaction in enumerate(self.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.borrowed_books.pop(i)
                break
        print(f"{member.name} returned '{book.title}'")
        return True
    
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