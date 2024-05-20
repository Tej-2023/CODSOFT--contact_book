import re

# Dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number (10 digits): ")
    while not re.match(r'^\d{10}$', phone_number):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone_number = input("Enter phone number (10 digits): ")
    email = input("Enter email address: ")
    while not re.match(r'^\w+@gmail\.com$', email):
        print("Invalid email address. Please enter a Gmail address.")
        email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone_number, 'email': email, 'address': address}
    print("Contact added successfully!")

def view_contact_list():
    print("Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if query in name or query == info['phone']:
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        print("Current Information:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
        phone_number = input("Enter new phone number (10 digits): ")
        while not re.match(r'^\d{10}$', phone_number):
            print("Invalid phone number. Please enter a 10-digit number.")
            phone_number = input("Enter new phone number (10 digits): ")
        email = input("Enter new email address: ")
        while not re.match(r'^\w+@gmail\.com$', email):
            print("Invalid email address. Please enter a Gmail address.")
            email = input("Enter new email address: ")
        address = input("Enter new address: ")
        contacts[name] = {'phone': phone_number, 'email': email, 'address': address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
