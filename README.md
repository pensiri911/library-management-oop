# OOP solution
## Overview
This project is about creating a library system that have member and borrowing 
learn how to design and use class

main goal of the assigment:
-Creating library system with OOP
-System must have add book, add member, borrow and return book

## Project structure
library-management-oop/
│
├── README.md                          # This file
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py                # Student's OOP implementation (to create)
│   └── test_oop.py                   # Tests for OOP version (to create)


---

## Design Overview

### Class: `Book`
**Purpose:**  
Represents a book in the library, including details like title, author, and how many copies are available.  

**Attributes:**  
- `id` (int): Unique identifier for the book  
- `title` (str): Title of the book  
- `author` (str): Author of the book  
- `available_copies` (int): Number of copies currently available  

**Key Methods:**  
- `borrow_book()`: Decreases the number of available copies by 1 when borrowed  
- `return_book()`: Increases the number of available copies by 1 when returned  

---

### Class: `Member`
**Purpose:**  
Represents a member of the library who can borrow and return books.  

**Attributes:**  
- `id` (int): Unique identifier for the member  
- `name` (str): Member’s full name  
- `email` (str): Member’s email address  
- `borrowed_books` (list): List of book IDs that the member has currently borrowed  

**Key Methods:**  
- `borrow(book_id)`: Adds a book ID to the member’s list of borrowed books  

---

### Class: `Library`
**Purpose:**  
Manages all operations in the library, including adding books and members, borrowing and returning books, and displaying information.  

**Attributes:**  
- `books` (list): List of all `Book` objects in the library  
- `members` (list): List of all `Member` objects registered in the library  
- `borrowed_books` (list): List of current borrowing transactions (each as a dictionary)  

**Key Methods:**  
- `add_book(book_id, title, author, available_copies)`: Adds a new book to the library  
- `add_member(member_id, name, email)`: Registers a new member  
- `borrow_book(member_id, book_id)`: Handles book borrowing logic with error checks  
- `return_book(member_id, book_id)`: Handles returning of books and updates records  
- `find_book(book_id)`: Finds and returns a book object by ID  
- `find_member(member_id)`: Finds and returns a member object by ID  
- `display_available_books()`: Displays all books that have available copies  
- `display_member_books(member_id)`: Displays all books currently borrowed by a member  

---

## 🧪 How to Test

### Option 1: Run in Python interactive shell
```python
from library import Library

# Create a Library instance
lib = Library()

# Add books
lib.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald", 2)
lib.add_book(2, "1984", "George Orwell", 1)

# Add members
lib.add_member(101, "Alice", "alice@email.com")
lib.add_member(102, "Bob", "bob@email.com")

# Borrow and return books
lib.borrow_book(101, 1)   # Alice borrows The Great Gatsby
lib.borrow_book(102, 2)   # Bob borrows 1984
lib.return_book(101, 1)   # Alice returns The Great Gatsby

# Display available books and member details
lib.display_available_books()
lib.display_member_books(101)

# Edge case
lib.borrow_book(999, 1)   # Invalid member ID
lib.borrow_book(101, 999) # Invalid book ID
lib.return_book(999, 1)   # Invalid member return
lib.return_book(101, 999) # Invalid book return