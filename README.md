# Mini Library Management System

## Overview
A simple Library Management System built with Python using **lists**, **dictionaries**, **tuples**, and **functions**.  
This system allows adding, searching, updating, deleting, borrowing, and returning books.

---

## Features
- Book Management: Add, update, search, and delete books
- Member Management: Add, update, and delete members
- Borrowing System: Members can borrow up to 3 books
- Return System: Members can return borrowed books
- Data Validation: Ensures unique ISBNs, valid genres, and proper borrowing limits

---

## Data Structures
- Books: Dictionary (ISBN → book details)
- Members: List of dictionaries (member details + borrowed books)
- Genres: Tuple of valid genres (Fiction, Non-Fiction, Sci-Fi)

---

## Installation
1. Clone this repository
2. Ensure Python 3.x is installed
3. No external dependencies required

---

## Usage

### Run Demo Script
```bash
python demo.py
```

### Run Unit Tests
```bash
python tests.py
```

---

## File Structure
```
📁 mini-library-system
│── operations.py   # Core functions (add, update, delete, borrow, return)
│── demo.py         # Demonstration script
│── tests.py        # Unit tests
│── README.md       # Documentation
```

---

## Example Output
```
🏛️ MINI LIBRARY MANAGEMENT SYSTEM DEMO
============================================================
 1. Adding Books
Book 'Harry Potter' added successfully.
Book '1984' added successfully.
...
 DEMO COMPLETED SUCCESSFULLY
============================================================
```
