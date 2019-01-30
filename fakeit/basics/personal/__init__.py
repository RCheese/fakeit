from . import emails
from . import names
from . import phones


class Person:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return f"<Person {self.fullname}> (FirstName={self.first_name}, LastName={self.last_name}, Email={self.email}, Phone={self.phone})"


def get_fake_person():
    first_name = names.get_name()
    last_name = names.get_surname()
    email = emails.fake_enough_email(addr=f"{first_name}.{last_name}")
    phone = phones.get_international()
    return Person(first_name=first_name, last_name=last_name, email=email, phone=phone)
