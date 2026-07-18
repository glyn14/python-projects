# views.py

from models import books


def show_books():
    print("\n--- ALL BOOKS ---")
    for book in books:
        status = "Borrowed" if book["borrowed"] else "Available"
        print(f"{book['title']} - {book['author']} ({status})")


def borrow_book():
    title = input("\nEnter book title to borrow: ")

    for book in books:
        if book["title"].lower() == title.lower():

            if book["borrowed"]:
                print("Book is already borrowed.")
            else:
                student = input("Enter student name: ")
                book["borrowed"] = True
                book["borrowed_by"] = student
                print("Book borrowed successfully!")
            return

    print("Book not found.")


def return_book():
    title = input("\nEnter book title to return: ")

    for book in books:
        if book["title"].lower() == title.lower():

            if book["borrowed"]:
                book["borrowed"] = False
                book["borrowed_by"] = ""
                print("Book returned successfully!")
            else:
                print("Book is already available.")
            return

    print("Book not found.")


def show_available():
    print("\n--- AVAILABLE BOOKS ---")

    for book in books:
        if not book["borrowed"]:
            print(f"{book['title']} - {book['author']}")


def show_borrowed():
    print("\n--- BORROWED BOOKS ---")

    for book in books:
        if book["borrowed"]:
            print(
                f"{book['title']} borrowed by {book['borrowed_by']}"
            )


while True:

    print("\n===== LIBRARY SYSTEM =====")
    print("1. Show All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Available Books")
    print("5. Show Borrowed Books")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        borrow_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        show_available()

    elif choice == "5":
        show_borrowed()

    elif choice == "6":
        print("Thank you for using Library System!")
        break

    else:
        print("Invalid choice.")