import csv

FILE_NAME = "library.csv"

# Add Book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author])

    print("Book Added Successfully!")

# Display Books
def display_books():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- Library Books ---")
            for row in reader:
                print("ID:", row[0], "| Title:", row[1], "| Author:", row[2])

    except FileNotFoundError:
        print("Error: Library file not found!")

# Search Book
def search_book():
    book_id = input("Enter Book ID to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            found = False
            for row in reader:
                if row[0] == book_id:
                    print("\nBook Found")
                    print("ID:", row[0])
                    print("Title:", row[1])
                    print("Author:", row[2])
                    found = True
                    break

            if not found:
                print("Book Not Found!")

    except FileNotFoundError:
        print("Error: Library file not found!")

# Remove Book
def remove_book():
    book_id = input("Enter Book ID to Remove: ")

    try:
        books = []

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] != book_id:
                    books.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)

        print("Book Removed Successfully!")

    except FileNotFoundError:
        print("Error: Library file not found!")

# Main Program
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Program Ended.")
        break
    else:
        print("Invalid Choice! Try Again.")