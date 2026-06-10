def load_contacts():

    contacts = {}

    file = open("contacts.txt", "r")

    for line in file:

        name, number = line.strip().split(",")

        contacts[name] = number

    file.close()

    return contacts


def save_contacts(contacts):

    file = open("contacts.txt", "w")

    for name, number in contacts.items():

        file.write(f"{name},{number}\n")

    file.close()


def display_contacts(contacts):

    print("\nAll Contacts")

    for name, number in contacts.items():

        print(name, "-", number)


def search_contact(contacts):

    name = input("Enter Contact Name: ")

    if name in contacts:

        print("Name   :", name)
        print("Number :", contacts[name])

    else:

        print("Contact Not Found")


def add_contact(contacts):

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    contacts[name] = number

    save_contacts(contacts)

    print("Contact Added Successfully")


def update_contact(contacts):

    name = input("Enter Name To Update: ")

    if name in contacts:

        new_number = input("Enter New Number: ")

        contacts[name] = new_number

        save_contacts(contacts)

        print("Contact Updated Successfully")

    else:

        print("Contact Not Found")


def delete_contact(contacts):

    name = input("Enter Name To Delete: ")

    if name in contacts:

        del contacts[name]

        save_contacts(contacts)

        print("Contact Deleted Successfully")

    else:

        print("Contact Not Found")


def vowel_contacts(contacts):

    vowels = "AEIOUaeiou"

    print("\nContacts Starting With Vowel")

    found = False

    for name, number in contacts.items():

        if name[0] in vowels:

            print(name, "-", number)

            found = True

    if not found:

        print("No Contact Starts With A Vowel")


def main():

    contacts = load_contacts()

    while True:

        print("\n===== Mobile Contact Directory System =====")
        print("1. Display All Contacts")
        print("2. Search Contact")
        print("3. Add Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Display Contacts Starting With Vowel")
        print("7. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            display_contacts(contacts)

        elif choice == 2:

            search_contact(contacts)

        elif choice == 3:

            add_contact(contacts)

            contacts = load_contacts()

        elif choice == 4:

            update_contact(contacts)

            contacts = load_contacts()

        elif choice == 5:

            delete_contact(contacts)

            contacts = load_contacts()

        elif choice == 6:

            vowel_contacts(contacts)

        elif choice == 7:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")


main()