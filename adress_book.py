from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Номер телефону має містити рівно 10 цифр")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False
    
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# ------------------------ Приклад використання ------------------------

if __name__ == "__main__":
    print("📘 Створюємо нову адресну книгу...")
    book = AddressBook()

    print("\n👤 Додаємо Alex:")
    alex_record = Record("Alex")
    alex_record.add_phone("1234567890")
    alex_record.add_phone("5555555555")
    book.add_record(alex_record)

    print("\n👤 Додаємо Olena:")
    olena_record = Record("Olena")
    olena_record.add_phone("9876543210")
    book.add_record(olena_record)

    print("\n📋 Всі записи в адресній книзі:")
    for name, record in book.data.items():
        print(record)

    print("\n✏️ Редагуємо телефон Alex:")
    alex = book.find("Alex")
    alex.edit_phone("1234567890", "1112223333")
    print(alex)

    print("\n🔍 Пошук телефону у Alex:")
    found_phone = alex.find_phone("5555555555")
    print(f"{alex.name}: {found_phone}")

    print("\n🗑 Видаляємо Olena з адресної книги:")
    book.delete("Olena")

    print("\n📋 Поточна адресна книга:")
    for name, record in book.data.items():
        print(record)
