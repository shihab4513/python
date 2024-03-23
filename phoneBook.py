
# You want to create a phonebook. You will search by name & want to find that person’s phone numbers in as low time cost as possible. The names are unique but a person may have multiple phone numbers. Which data structure will you use & how will you use it to store mobile numbers for each person? Code this in python

class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, numbers):
        if name in self.phonebook:
            self.phonebook[name].extend(numbers)
        else:
            self.phonebook[name] = numbers

    def get_numbers(self, name):
        return self.phonebook.get(name, "Contact not found.")

# Create a PhoneBook object
phonebook = PhoneBook()

# Add contacts
phonebook.add_contact("Alice", ["123-456-7890", "234-567-8901"])
phonebook.add_contact("Alice", ["567-456-7890", "345-567-8901"])
phonebook.add_contact("Bob", ["345-678-9012"])

# Get phone numbers
print(phonebook.get_numbers("Alice"))  # Output: ['123-456-7890', '234-567-8901']
print(phonebook.get_numbers("Bob"))  # Output: ['345-678-9012']
print(phonebook.get_numbers("Charlie"))  # Output: Contact not found.
