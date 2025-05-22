# CLI Contact Book

contacts = []  # List to store contact dictionaries

def display_menu():
    print("\nWelcome to CLI Contact Book")
    print("Select an option e.g: 1, 2, or 3")
    print("1. Add New Contact")
    print("2. View All Saved Contacts")
    print("3. Exit the application")

def add_contact():
    name = input("Enter Full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    print(f"Contact '{name}' saved successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nSaved Contacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    while True:
        display_menu()
        choice = input("Your choice: ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
