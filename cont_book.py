contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print("Contact Added!")

    elif choice == "2":
        print("\nContact List:")
        for contact in contacts:
            print(contact["name"], "-", contact["phone"])

    elif choice == "3":
        search = input("Enter Name or Phone: ")
        found = False

        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print(contact)
                found = True

        if not found:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("New Phone: ")
                contact["email"] = input("New Email: ")
                contact["address"] = input("New Address: ")
                print("Contact Updated!")
                break

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact Deleted!")
                break

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice!")