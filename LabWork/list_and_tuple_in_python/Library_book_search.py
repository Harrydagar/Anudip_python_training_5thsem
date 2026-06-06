"""
5. Library Book Search
Problem Statement
Books available in a library:
books = [ ("Python Basics", 5), ("Data Science", 0), ("Java Programming", 3), ("Machine Learning", 0) ]
Write a program to:
•
Display unavailable books.
•
Find all books with more than 2 copies.
•
Count available books.
•
Stop searching once a requested book is found.
"""

# Book name and available copies
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

available_books = 0

print("Unavailable Books:")

for book in books:

    # Display unavailable books
    if book[1] == 0:
        print(book[0])

    # Count available books
    if book[1] > 0:
        available_books += 1

print("\nBooks With More Than 2 Copies:")

for book in books:
    if book[1] > 2:
        print(book[0])

print("\nAvailable Books:", available_books)

# Search for a book
search_book = "Java Programming"

for book in books:
    if book[0] == search_book:
        print("\nBook Found:", book[0])
        break

