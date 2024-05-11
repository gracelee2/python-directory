#Grace Lee
#08/31/2023
# lab 2


def add_contact(contacts, id, first_name, last_name):
  """
  Asks the user for a contact and their names and adds them to the dictionary.
  If the id/phone number is already in the contact dictionary, it throws an error.
  
  """
  if id in contacts:
    print("Phone number already exists.")
    return 'error'
  else:
    contacts[id] = [first_name, last_name]
    print("Added : ")
    print(contacts.get(id))
    return True


def modify_contact(contacts, id, first_name, last_name):
  """
  Asks them for a contact, and if the contact is not in the dictionary it throws an error. 
  If not, it asks the user for th new contact information and replaces it.
  
  """
  if id not in contacts:
    print("Phone number does not exist.")
    return 'error'
  else:
    contacts[id] = [first_name, last_name]
    print("Modified : ")
    print(contacts.get(id))
    return True


def delete_contact(contacts, id):
  """
  Asks which id/phone number the user wants to delete. 
  If the number is not in the dictionary, it throws an error.
  
  """
  if id not in contacts:
    print("Error:Phone number doesn't exist")
    return 'error'
  else:
    del_contact = contacts.get(id)
    del contacts[id]
    print("Deleted : ")
    print(del_contact)
    return True


def sort_contacts(contacts):
  """
  Sorts the dictionary last name first, then first name. It then returns the sorted dictionary.
  
  """
  sorted_dict = dict(
      sorted(contacts.items(),
             key=lambda x: (x[1][1].lower(), x[1][0].lower())))
  print(sorted_dict)
  return sorted_dict

def find_contact(contacts, find):
  """
  Asks the user for a string or number to search through the dictionary. 
  If the string is found in the dictionary, function returns a new dictionary with the values that match the input.
  
  """
  temp = {}
  for key, value in contacts.items():
    if find is not None and find.isnumeric() and find.lower(
    ) in value[0].lower() or find.lower() in value[1].lower():
      temp[key] = value
  if find.isnumeric():
    num_find = int(find)
    if num_find in contacts:
      temp[num_find] = contacts[num_find]
  elif find.isnumeric() is False:
    if contacts.get(find):
      temp[find] = contacts.get(find)
    sorted_dict = dict(
        sorted(contacts.items(),
               key=lambda x: (x[1][1].lower(), x[1][0].lower())))
    print(sorted_dict)
  else:
    return 'error'
