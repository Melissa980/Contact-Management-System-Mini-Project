import os
import re

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    if phone_number in contacts:
        print("Contact with this phone number already exists.")
        return
    
    email = input("Enter email: ")
    address = input("Enter address (optional): ")
    notes = input("Enter additional notes (optional): ")

    contacts[phone_number] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully.")

def edit_contact():
    phone_number = input("Enter phone number of the contact to edit: ")
    if phone_number not in contacts:
        print("Contact not found.")
        return
    
    print("Enter new details (leave blank to keep current value):")
    name = input(f"Name ({contacts[phone_number]['name']}): ") or contacts[phone_number]['name']
    email = input(f"Email ({contacts[phone_number]['email']}): ") or contacts[phone_number]['email']
    address = input(f"Address ({contacts[phone_number]['address']}): ") or contacts[phone_number]['address']
    notes = input(f"Notes ({contacts[phone_number]['notes']}): ") or contacts[phone_number]['notes']
    
    contacts[phone_number] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact updated successfully.")

def delete_contact():
    phone_number = input("Enter phone number of the contact to delete: ")
    if phone_number in contacts:
        del contacts[phone_number]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    search_term = input("Enter name, phone number, or email to search: ")
    for phone_number, details in contacts.items():
        if (search_term in details['name'] or
            search_term in phone_number or
            search_term in details['email']):
            print(f"Found contact - Phone: {phone_number}, Name: {details['name']}, Email: {details['email']}")
            return
    print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for phone_number, details in contacts.items():
        print(f"Phone: {phone_number}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}")

def export_contacts():
    filename = input("Enter the filename to export contacts: ")
    with open(filename, 'w') as f:
        for phone_number, details in contacts.items():
            f.write(f"{phone_number},{details['name']},{details['email']},{details['address']},{details['notes']}\n")
    print("Contacts exported successfully.")

def import_contacts():
    filename = input("Enter the filename to import contacts from: ")
    try:
        with open(filename, 'r') as f:
            for line in f:
                phone_number, name, email, address, notes = line.strip().split(',')
                contacts[phone_number] = {
                    'name': name,
                    'email': email,
                    'address': address,
                    'notes': notes
                }
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file *BONUS*")
        print("8. Quit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
