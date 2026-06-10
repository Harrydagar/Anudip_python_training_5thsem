def load_books():
    books = []

    file = open("books.txt", "r")

    for line in file:
        book_id, title, quantity = line.strip().split(",")

        books.append(
            {
                "id": book_id,
                "title": title,
                "quantity": int(quantity)
            }
        )

    file.close()

    return books


def save_books(books):

    file = open("books.txt", "w")

    for book in books:
        file.write(
            f"{book['id']},{book['title']},{book['quantity']}\n"
        )

    file.close()


def display_books(books):

    print("\nAvailable Books")

    for book in books:
        print(book["id"], "-", book["title"],
              "- Quantity:", book["quantity"])


def search_book(books):

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            print("\nBook Found")
            print("Book ID :", book["id"])
            print("Title   :", book["title"])
            print("Copies  :", book["quantity"])

            return

    print("Book not found")


def issue_book(books):

    book_id = input("Enter Book ID to Issue: ")

    for book in books:

        if book["id"] == book_id:

            if book["quantity"] > 0:

                book["quantity"] -= 1

                save_books(books)

                print("Book Issued Successfully")

            else:

                print("Book Not Available")

            return

    print("Book ID not found")


def return_book(books):

    book_id = input("Enter Book ID to Return: ")

    for book in books:

        if book["id"] == book_id:

            book["quantity"] += 1

            save_books(books)

            print("Book Returned Successfully")

            return

    print("Book ID not found")


def unavailable_books(books):

    print("\nUnavailable Books")

    found = False

    for book in books:

        if book["quantity"] == 0:

            print(book["id"], "-", book["title"])

            found = True

    if not found:
        print("No unavailable books")


def restocking_books(books):

    print("\nBooks Requiring Restocking")

    found = False

    for book in books:

        if book["quantity"] < 2:

            print(book["id"], "-", book["title"],
                  "- Quantity:", book["quantity"])

            found = True

    if not found:
        print("No books require restocking")


def main():

    books = load_books()

    while True:

        print("\n===== Library Book Issue System =====")
        print("1. Display All Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Unavailable Books")
        print("6. Display Books Requiring Restocking")
        print("7. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            display_books(books)

        elif choice == 2:

            search_book(books)

        elif choice == 3:

            issue_book(books)

            books = load_books()

        elif choice == 4:

            return_book(books)

            books = load_books()

        elif choice == 5:

            unavailable_books(books)

        elif choice == 6:

            restocking_books(books)

        elif choice == 7:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")


main()