from collections import UserDict


class Field:
    pass


class AddressBook(UserDict, Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_record(self, record):
        self.data[record.name.value] = record


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record(Field):
    def __init__(self):
        self.name = Name
        self.phone = Phone

    def add_contact(self, new_name, new_phone):
        self.name = self.name(new_name)
        self.phone = self.phone(new_phone)

    def edit_contact(self, cls, contact_name, new_phone):
        if contact_name in cls.data:
            self.name = self.name(contact_name)
            self.phone = self.phone(new_phone)


def main():
    adressbook = AddressBook()

    while True:
        a = input('Enter command:\n').lower()
        if a == '.':
            break
        elif a in ("good bye", "close", "exit"):
            print("Good Bye!")
            break
        elif a == 'hello':
            print('How can I help you?')
        elif a == 'show all':  # Show all contacts
            print(adressbook.data)
        elif a == 'show':  # Show one contact
            name = input('Enter name:\n')
            print(adressbook.data[name].name.value, 'phone:', adressbook.data[name].phone.value)
        elif a.split()[0] == 'add':  # Add contact
            name = input('Enter name:\n')
            phone = input('Enter phone: \n')
            if name and phone:
                record_add = Record()
                record_add.add_contact(name.lower(), phone.split() if ' ' in phone else [phone])
                adressbook.add_record(record_add)
            else:
                print('Enter correct name and phone')
        elif a.split()[0] == 'change':  # Add contact number
            name = input('Enter name:\n')
            phone = input('Enter phone: \n')
            try:
                adressbook.data[name].phone.value.append(phone)
            except KeyError:
                print('Wrong name entered')
        elif a.split()[0] == 'delete':  # Delete contact number
            name = input('Enter name:\n')
            phone = input('Enter phone which you want to delete: \n')
            try:
                adressbook.data[name].phone.value.remove(phone)
            except KeyError:
                print('Wrong name entered')
            except ValueError:
                print('The phone number not exist')


if __name__ == '__main__':
    main()
