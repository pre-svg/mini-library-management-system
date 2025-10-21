# operations.py - Library Management System (OOP Version)

VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")


class Book:
    def __init__(self, isbn, title, author, genre, total_copies):
        if genre not in VALID_GENRES:
            raise ValueError(f"Invalid genre. Must be one of {VALID_GENRES}")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies

    def update(self, **kwargs):
        if "genre" in kwargs and kwargs["genre"] not in VALID_GENRES:
            return False, f"Invalid genre. Must be one of {VALID_GENRES}"
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return True, "Book updated successfully"


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

    def borrow(self, isbn):
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)


class Library:
    def __init__(self):
        self.books = {}      # isbn -> Book object
        self.members = {}    # member_id -> Member object

    # ---------- Book Operations ----------
    def add_book(self, isbn, title, author, genre, total_copies):
        if isbn in self.books:
            return False, "ISBN already exists"
        try:
            self.books[isbn] = Book(isbn, title, author, genre, total_copies)
            return True, "Book added successfully"
        except ValueError as e:
            return False, str(e)

    def search_books(self, query):
        query = query.lower()
        results = []
        for book in self.books.values():
            if query in book.title.lower() or query in book.author.lower():
                results.append({
                    "isbn": book.isbn,
                    "title": book.title,
                    "author": book.author,
                    "genre": book.genre,
                    "total_copies": book.total_copies,
                    "available_copies": book.available_copies
                })
        return results

    def update_book(self, isbn, **kwargs):
        if isbn not in self.books:
            return False, "Book not found"
        return self.books[isbn].update(**kwargs)

    def delete_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            return False, "Book not found"
        if book.available_copies < book.total_copies:
            return False, "Cannot delete book with borrowed copies"
        del self.books[isbn]
        return True, "Book deleted successfully"

    # ---------- Member Operations ----------
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            return False, "Member ID already exists"
        self.members[member_id] = Member(member_id, name, email)
        return True, "Member added successfully"

    def update_member(self, member_id, **kwargs):
        member = self.members.get(member_id)
        if not member:
            return False, "Member not found"
        for key, value in kwargs.items():
            if hasattr(member, key) and key != "borrowed_books":
                setattr(member, key, value)
        return True, "Member updated successfully"

    def delete_member(self, member_id):
        member = self.members.get(member_id)
        if not member:
            return False, "Member not found"
        if member.borrowed_books:
            return False, "Cannot delete member with borrowed books"
        del self.members[member_id]
        return True, "Member deleted successfully"

    # ---------- Borrow / Return ----------
    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            return False, "Member not found"
        if not book:
            return False, "Book not found"
        if not member.can_borrow():
            return False, "Member has reached borrowing limit (3 books)"
        if book.available_copies <= 0:
            return False, "No copies available"
        if isbn in member.borrowed_books:
            return False, "Member already borrowed this book"

        book.available_copies -= 1
        member.borrow(isbn)
        return True, "Book borrowed successfully"

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            return False, "Member not found"
        if not book:
            return False, "Book not found"
        if isbn not in member.borrowed_books:
            return False, "Member has not borrowed this book"

        book.available_copies += 1
        member.return_book(isbn)
        return True, "Book returned successfully"

