# demo.py - Demonstration of Library Management System (OOP Version)

from operations import Library


def print_section(title):
    print(f"\n{'=' * 60}")
    print(f" {title}")
    print(f"{'=' * 60}")


def main():
    library = Library()
    print("\n🏛️  MINI LIBRARY MANAGEMENT SYSTEM DEMO")
    print("=" * 60)

    # 1. Add Books
    print_section("1. Adding Books")
    print(library.add_book("978-0-7475-3269-9", "Harry Potter", "J.K. Rowling", "Fiction", 5))
    print(library.add_book("978-0-553-29335-0", "1984", "George Orwell", "Fiction", 3))
    print(library.add_book("978-0-345-39180-3", "Dune", "Frank Herbert", "Sci-Fi", 4))
    print(library.add_book("978-0-062-31609-8", "Sapiens", "Yuval Noah Harari", "Non-Fiction", 2))
    print(f"\nTotal books in library: {len(library.books)}")

    # 2. Add Members
    print_section("2. Adding Members")
    print(library.add_member("M001", "Alice Johnson", "alice@email.com"))
    print(library.add_member("M002", "Bob Smith", "bob@email.com"))
    print(library.add_member("M003", "Carol Davis", "carol@email.com"))
    print(f"\nTotal members: {len(library.members)}")

    # 3. Search Books
    print_section("3. Searching Books")
    results = library.search_books("Harry")
    print(f"Search results for 'Harry': {len(results)} found")
    for book in results:
        print(f"  - {book['title']} by {book['author']} (ISBN: {book['isbn']})")

    results = library.search_books("Orwell")
    print(f"\nSearch results for 'Orwell': {len(results)} found")
    for book in results:
        print(f"  - {book['title']} by {book['author']}")

    # 4. Borrow Books
    print_section("4. Borrowing Books")
    print(library.borrow_book("M001", "978-0-7475-3269-9"))  # Alice borrows Harry Potter
    print(library.borrow_book("M001", "978-0-553-29335-0"))  # Alice borrows 1984
    print(library.borrow_book("M002", "978-0-345-39180-3"))  # Bob borrows Dune
    print(f"\nAlice's borrowed books: {library.members['M001'].borrowed_books}")

    # 5. Testing Borrow Limits
    print_section("5. Testing Borrow Limits")
    for i in range(3):
        result = library.borrow_book("M003", "978-0-062-31609-8")
        print(f"Attempt {i + 1}: {result}")

    # 6. Return Books
    print_section("6. Returning Books")
    print(library.return_book("M001", "978-0-7475-3269-9"))  # Alice returns Harry Potter
    print(f"Alice's borrowed books after return: {library.members['M001'].borrowed_books}")

    # 7. Update Book
    print_section("7. Updating Book Details")
    print(library.update_book("978-0-345-39180-3", total_copies=6, available_copies=5))
    dune = library.books["978-0-345-39180-3"]
    print(
        f"Updated Dune: {{'title': dune.title, 'total_copies': dune.total_copies, 'available_copies': dune.available_copies}}")

    # 8. Delete Operations
    print_section("8. Testing Delete Operations")
    print(library.delete_book("978-0-553-29335-0"))  # Should fail (borrowed by Alice)
    print(library.delete_member("M001"))  # Should fail (has borrowed books)

    # Return remaining and delete
    print(library.return_book("M001", "978-0-553-29335-0"))
    print(library.delete_member("M001"))  # Should now succeed
    print(f"\nTotal members after deletion: {len(library.members)}")

    print("\n" + "=" * 60)
    print(" DEMO COMPLETED SUCCESSFULLY")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
