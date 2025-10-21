# tests.py - Unit tests for Library Management System (OOP Version)

from operations import Library


def test_add_book_success():
    """Test 1: Successfully add a book with valid data"""
    lib = Library()
    success, msg = lib.add_book("978-1-234-56789-0", "Test Book", "Test Author", "Fiction", 5)
    assert success is True, "Should successfully add a valid book"
    assert "978-1-234-56789-0" in lib.books, "Book should be stored in library"
    assert lib.books["978-1-234-56789-0"].available_copies == 5, "Available copies should match total copies"
    print("✓ Test 1 passed: Add book with valid data")


def test_add_book_duplicate_isbn():
    """Test 2: Fail to add book with duplicate ISBN"""
    lib = Library()
    lib.add_book("978-1-234-56789-0", "Book 1", "Author", "Fiction", 5)
    success, msg = lib.add_book("978-1-234-56789-0", "Book 2", "Author", "Sci-Fi", 3)
    assert success is False, "Should fail to add book with duplicate ISBN"
    print("✓ Test 2 passed: Reject duplicate ISBN")


def test_add_book_invalid_genre():
    """Test 3: Fail to add book with invalid genre"""
    lib = Library()
    success, msg = lib.add_book("978-1-234-56789-1", "Test Book", "Author", "Romance", 5)
    assert success is False, "Should fail to add book with invalid genre"
    assert "978-1-234-56789-1" not in lib.books, "Book should not be added"
    print("✓ Test 3 passed: Reject invalid genre")


def test_borrow_limit():
    """Test 4: Member cannot borrow more than 3 books"""
    lib = Library()
    lib.add_member("M001", "Test User", "test@email.com")
    for i in range(4):
        lib.add_book(f"ISBN-{i}", f"Book {i}", "Author", "Fiction", 5)

    for i in range(3):
        success, msg = lib.borrow_book("M001", f"ISBN-{i}")
        assert success is True, f"Should successfully borrow book {i + 1}"

    success, msg = lib.borrow_book("M001", "ISBN-3")
    assert success is False, "Should fail to borrow 4th book"
    assert "limit" in msg.lower(), "Error message should mention borrowing limit"
    print("✓ Test 4 passed: Enforce 3-book borrowing limit")


def test_borrow_when_no_copies():
    """Test 5: Cannot borrow when no copies available"""
    lib = Library()
    lib.add_book("ISBN-001", "Popular Book", "Author", "Fiction", 1)
    lib.add_member("M001", "User 1", "user1@email.com")
    lib.add_member("M002", "User 2", "user2@email.com")

    success1, _ = lib.borrow_book("M001", "ISBN-001")
    assert success1 is True, "First borrow should succeed"

    success2, _ = lib.borrow_book("M002", "ISBN-001")
    assert success2 is False, "Second borrow should fail when no copies"
    assert lib.books["ISBN-001"].available_copies == 0
    print("✓ Test 5 passed: Cannot borrow when no copies available")


def test_delete_book_with_borrowed_copies():
    """Test 6: Cannot delete book if copies are borrowed"""
    lib = Library()
    lib.add_book("ISBN-001", "Book", "Author", "Fiction", 2)
    lib.add_member("M001", "User", "user@email.com")
    lib.borrow_book("M001", "ISBN-001")

    success, _ = lib.delete_book("ISBN-001")
    assert success is False, "Should fail to delete book with borrowed copies"
    assert "ISBN-001" in lib.books
    print("✓ Test 6 passed: Cannot delete book with borrowed copies")


def test_search_books():
    """Test 7: Search books by title and author"""
    lib = Library()
    lib.add_book("ISBN-001", "Python Programming", "John Smith", "Non-Fiction", 3)
    lib.add_book("ISBN-002", "Java Basics", "Jane Doe", "Non-Fiction", 2)
    lib.add_book("ISBN-003", "Advanced Python", "John Smith", "Non-Fiction", 4)

    results = lib.search_books("Python")
    assert len(results) == 2, "Should find 2 books with 'Python' in title"

    results = lib.search_books("John Smith")
    assert len(results) == 2, "Should find 2 books by John Smith"
    print("✓ Test 7 passed: Search functionality works correctly")


def test_return_book():
    """Test 8: Return borrowed book successfully"""
    lib = Library()
    lib.add_book("ISBN-001", "Book", "Author", "Fiction", 3)
    lib.add_member("M001", "User", "user@email.com")

    initial = lib.books["ISBN-001"].available_copies
    lib.borrow_book("M001", "ISBN-001")
    assert lib.books["ISBN-001"].available_copies == initial - 1

    lib.return_book("M001", "ISBN-001")
    assert lib.books["ISBN-001"].available_copies == initial
    assert "ISBN-001" not in lib.members["M001"].borrowed_books
    print("✓ Test 8 passed: Return book successfully")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print(" RUNNING UNIT TESTS")
    print("=" * 60 + "\n")

    test_add_book_success()
    test_add_book_duplicate_isbn()
    test_add_book_invalid_genre()
    test_borrow_limit()
    test_borrow_when_no_copies()
    test_delete_book_with_borrowed_copies()
    test_search_books()
    test_return_book()

    print("\n" + "=" * 60)
    print(" ALL TESTS PASSED ✓")
    print("=" * 60 + "\n")
