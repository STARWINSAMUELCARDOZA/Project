#Assignment
#WAP to maintain phonebook with a name and phone number 
# declare four methods such as add new contact, remove existing contact,
# search the contat with help of contact name and display.

# contact = {
#     "granny" : 9980093121,
#     "sam" : 1234567890,
#     "me" : 7892247442
# }

# def addContact(name,phone):
#     contact[name]=phone
#     print(f"contact number is added: {name}")
# addContact('abc',2345678901)
# print(contact)

# def removeContact(name,phone):
#     contact[name]=phone
#     print(f"contact number is removed: {name}")
# removeContact.__reduce__('abc',2345678901)
# print(contact)

phonebook = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    phonebook[name] = phone
    print("Added.")

def remove_contact():
    name = input("Name to remove: ")
    if name in phonebook:
        del phonebook[name]
        print("Removed.")
    else:
        print("Not found.")

def search_contact():
    name = input("Name to search: ")
    print(f"{name}: {phonebook.get(name, 'Not found')}")

def display_contacts():
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

while True:
    print("\n1.Add 2.Remove 3.Search 4.Display 5.Exit")
    choice = input("Choice: ")
    if choice == '1': add_contact()
    elif choice == '2': remove_contact()
    elif choice == '3': search_contact()
    elif choice == '4': display_contacts()
    elif choice == '5': break
    else: print("Invalid")