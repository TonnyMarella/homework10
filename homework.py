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
    def __init__(self, new_name):
        self.name = Name(new_name)
        self.phone = []

    def add_contact(self, new_phone):
        self.phone.append(Phone(new_phone))

    def edit_contact(self, cls, contact_name, new_phone):
        if contact_name in cls.data:
            self.name = self.name(contact_name)
            self.phone = self.phone(new_phone)


def get_name_and_phone():
    """
    To avoid duplication
    """
    name = input('Enter name:\n')
    phone = input('Enter one phone number: \n')
    return name, phone


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
            print('name:', adressbook.data[name].name.value, 'phone:',
                  list(map(lambda x: x.value, adressbook.data[name].phone)))
        elif a.split()[0] == 'add':  # Add contact
            name, phone = get_name_and_phone()
            if len(phone.split()) > 1:
                print('Enter ONE phone number')
            else:
                if name and phone:
                    record_add = Record(name.lower())
                    record_add.add_contact(phone)
                    adressbook.add_record(record_add)
                else:
                    print('Enter correct name and phone')
        elif a.split()[0] == 'change':  # Add contact number
            name, phone = get_name_and_phone()
            try:
                record_change = adressbook.data[name]
                record_change.add_contact(phone)
                adressbook.add_record(record_change)
            except KeyError:
                print('Wrong name entered')
        elif a.split()[0] == 'delete':  # Delete contact number
            name, phone = get_name_and_phone()
            try:
                record_delete = adressbook.data[name]
                need_to_delete = list(filter(lambda x: x.value == phone, record_delete.phone))
                record_delete.phone.remove(need_to_delete[0])
                adressbook.add_record(record_delete)
            except KeyError:
                print('Wrong name entered')
            except IndexError:
                print('The phone number not exist')


if __name__ == '__main__':
    main()
