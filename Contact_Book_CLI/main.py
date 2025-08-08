# import json
# import os

# def load_contacts():
#     if not os.path.exists("./contacts.json"):
#         return []
#     with open("./contacts.json","r") as file:
#         return json.load(file)
    
# def save_contacts(contacts):
#     with open("./contacts.json","w") as file:
#         json.dump(contacts, file, indent=4)
        
# def add_contact():
#     name = input("Enter the name")
#     phone = input("Enter mobile number")
#     email = input("Enter email")
    
#     contacts = load_contacts()
#     contacts.append({"name":name,"phone":phone,"email":email})
#     save_contacts(contacts)
#     print("Contact added successfully")
#     print(contacts)
    
    
# def search_contact():
#     name = input("Enter the name")
    
#     contacts = load_contacts()
#     for contact in contacts:
#         if contact["name"] == name:
#             print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
#         else:
#             print("Contact not found")
#     print(contacts)
    
            

# def update_contact():
#     name = input("Enter contact name")
#     contacts = load_contacts()
#     for i in range(len(contacts)):
#         if contacts[i]["name"] == name:
#             contacts[i]["phone"] = input("Enter new phone number")
#             contacts[i]["email"] = input("Enter new email")
#             save_contacts(contacts)
#             print("Contact updated successfully")
#         else:
#             print("Contact not found")
#     print(contacts)
    

# def delete_contact():
#     name = input("Enter the name")
#     contacts = load_contacts()
#     new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    
#     if (len(contacts) != len(new_contacts)):
#         save_contacts(new_contacts)
#         print("Contact deleted successfully")
#     else:
#         print("Contact not found")
#     print(new_contacts)
    


# def main():
#     while True:
#         print("Contact Book")
#         print("\n1. Add Contact")
#         print("\n2. Search Contact")
#         print("\n3. Update Contact")
#         print("\n4. Delete Contact")
#         print("\n5. Exit")
    
#         choice = input("Enter your choice")
        
#         match choice:
#             case "1":
#                 add_contact()
#             case "2":
#                 search_contact()
#             case "3":
#                 update_contact()
#             case "4":
#                 delete_contact()
#             case "5":
#                 print("Exiting the Contact Book")
#                 break
#             case _:
#                 print("Invalid choice. Please choose a valid option")
        


# if __name__ == "__main__":
#     main()


import json
import os

CONTACTS_FILE = "contacts.json"


# ------------------- Utility Functions -------------------
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# ------------------- Operations -------------------
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")
    contacts = load_contacts()
    found = [c for c in contacts if name.lower() in c["name"].lower()]

    if found:
        print("🔎 Found contacts:")
        for c in found:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("❌ No contact found.")


def update_contact():
    name = input("Enter name to update: ")
    contacts = load_contacts()

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Leave blank to keep current value.")
            new_phone = input(f"Enter new phone ({c['phone']}): ") or c["phone"]
            new_email = input(f"Enter new email ({c['email']}): ") or c["email"]
            c["phone"], c["email"] = new_phone, new_email
            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")


# ------------------- Main CLI -------------------
def main():
    while True:
        print("\n📖 Contact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
