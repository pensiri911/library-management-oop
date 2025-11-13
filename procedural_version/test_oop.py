from library_oop import *
def test():
    library = Library()
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")
    print("\n--- TEST 3: Display Available Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python Crash Course
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python Crash Course
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    library.display_available_books()
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(101, 4)  # Alice's 3rd book
    library.display_member_books(101)
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    library.borrow_book(102, 3)  # Bob tries to borrow unavailable book
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)  # Alice returns Python Crash Course
    library.return_book(102, 1)  # Bob returns Python Crash Course
    library.display_member_books(101)
    library.display_available_books()
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)  # Bob tries to return book he didn't borrow
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)  # Carol returns Pragmatic Programmer
    library.borrow_book(102, 3)  # Bob borrows it
    library.display_member_books(102)
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)  # Non-existent member
    library.borrow_book(101, 999)  # Non-existent book
    library.return_book(999, 1)  # Non-existent member
    library.display_member_books(999)  # Non-existent member
    print()
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in library.borrowed_books:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    
    print("\nAll Members and Their Books:")
    for member in library.members:
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            for book_id in member.borrowed_books:
                book = library.find_book(book_id)
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")
    
    library.display_available_books()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
if __name__ == "__main__":
    test()