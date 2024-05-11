import contacts

def main():
  contact = {}
  while True:

    print("Menu\n")
    print("1.Add contact\n")
    print("2.Modify Contact\n")
    print("3.Delete Contact\n")
    print("4.Print contact list\n")
    print("5.Find contact\n")
    print("6. Exit the program\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        id = int(input("Enter phone number: "))
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        contacts.add_contact(id,first_name, last_name)
    elif choice == 2:
        id = int(input("Enter phone number: "))
        first_name = input("Enter the new first name: ")
        last_name = input("Enter the new last name: ")
        contacts.modify_contact(id, first_name, last_name)
    elif choice == 3:
         id = int(input("Enter phone number: "))
         contacts.delete_contact(id)
    elif choice == 4:
        contacts.sort_contacts(contact)
    elif choice == 5:
        find = input("Enter search string: ")
        contacts.find_contact(contact, find)
    elif choice == 6:
      print("Goodbye")
      break
    else:
      print("Not an option, choose again")


main()
