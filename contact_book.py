# Contact Book

contacts = {}

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone
    print("Contact Added Successfully!")

# View Contacts
def view_contacts():
    if not contacts:
        print("No Contacts Found!")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)

# Search Contact
def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Contact Not Found!")

# Delete Contact
def delete_contact():
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

# Main Program
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")