"""3. Smart Library Management System
Problem Statement
Create a digital library management system.
Example Structure
library = { "B101": { "title": "Python Basics", "author": "ABC", "copies": 5 } }
Maintain records of at least 30 books.
Requirements
1.
Add a book.
2.
Remove a book.
3.
Search a book by ID.
4.
Search by title.
5.
Update available copies.
6.
Issue a book.
7.
Return a book.
8.
Display books with fewer than 3 copies.
9.
Display books that are unavailable.
10.
Find the most available book.
11.
Generate a restocking report.
12.
Create a separate dictionary of books requiring immediate purchase.
Challenge
Generate a complete library summary report."""
# ==========================================
# SMART LIBRARY MANAGEMENT SYSTEM
# ==========================================

library = {
"B101":{"title":"Python Basics","author":"ABC","copies":5},
"B102":{"title":"Java Programming","author":"XYZ","copies":2},
"B103":{"title":"C Language","author":"PQR","copies":4},
"B104":{"title":"Data Structures","author":"John","copies":3},
"B105":{"title":"Algorithms","author":"Martin","copies":1},
"B106":{"title":"DBMS","author":"Korth","copies":6},
"B107":{"title":"Operating Systems","author":"Galvin","copies":2},
"B108":{"title":"Computer Networks","author":"Tanenbaum","copies":4},
"B109":{"title":"Machine Learning","author":"Tom","copies":5},
"B110":{"title":"Artificial Intelligence","author":"Russell","copies":1},
"B111":{"title":"Cyber Security","author":"James","copies":3},
"B112":{"title":"Cloud Computing","author":"David","copies":2},
"B113":{"title":"Big Data","author":"Andrew","copies":4},
"B114":{"title":"Web Development","author":"Mark","copies":5},
"B115":{"title":"Django","author":"William","copies":2},
"B116":{"title":"Flask","author":"Robert","copies":3},
"B117":{"title":"JavaScript","author":"Kevin","copies":4},
"B118":{"title":"React","author":"Chris","copies":1},
"B119":{"title":"NodeJS","author":"Steve","copies":2},
"B120":{"title":"MongoDB","author":"Thomas","copies":5},
"B121":{"title":"Power BI","author":"Emma","copies":3},
"B122":{"title":"Excel Advanced","author":"Sophia","copies":4},
"B123":{"title":"Statistics","author":"Miller","copies":2},
"B124":{"title":"Mathematics","author":"Brown","copies":5},
"B125":{"title":"Physics","author":"Wilson","copies":3},
"B126":{"title":"Chemistry","author":"Taylor","copies":2},
"B127":{"title":"Biology","author":"Clark","copies":1},
"B128":{"title":"English Grammar","author":"Scott","copies":4},
"B129":{"title":"Economics","author":"Lewis","copies":2},
"B130":{"title":"Business Studies","author":"Walker","copies":5}
}

# ==========================================
# FUNCTIONS
# ==========================================

def display_books():
    print("\nBOOK RECORDS")
    print("-" * 70)

    for bid in library:
        book = library[bid]

        print(
            bid,
            "|", book["title"],
            "|", book["author"],
            "| Copies:", book["copies"]
        )


def add_book():

    bid = input("Enter Book ID: ")

    if bid in library:
        print("Book ID already exists")
        return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Copies: "))

    library[bid] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print("Book Added Successfully")


def remove_book():

    bid = input("Enter Book ID: ")

    if bid in library:
        del library[bid]
        print("Book Removed Successfully")
    else:
        print("Book Not Found")


def search_by_id():

    bid = input("Enter Book ID: ")

    if bid in library:

        print("\nBOOK FOUND")
        print("Title :", library[bid]["title"])
        print("Author:", library[bid]["author"])
        print("Copies:", library[bid]["copies"])

    else:
        print("Book Not Found")


def search