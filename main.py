from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"[0-9]{10}", str(value)):
            raise ValueError("Invalid  phone number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone):
        phone = Phone(new_phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone is None:
            raise ValueError(f"Phone {old_phone} not found for {self.name.value}")
        new_phone = Phone(new_phone)
        phone.value = new_phone.value

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        clear_phone = self.find_phone(phone)
        if clear_phone is None:
            raise ValueError(f"Phone {phone} not found for {self.name.value}")
        self.phones.remove(clear_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, person):
        self.data[person.name.value] = person
        return f"Contact {person.name.value} added."

    def find(self, person_name):
        return self.data.get(person_name)

    def delete(self, person_name):
        del self.data[person_name]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")

john.edit_phone("1234567890", "1112223333")

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")

