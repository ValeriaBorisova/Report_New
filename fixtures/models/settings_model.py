from faker import Faker
fake = Faker("Ru-ru")


class SettingsData:
    def __init__(self, name=None, lastname=None, email=None, city=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.city = city

    @staticmethod
    def random():
        email = fake.email()
        name = fake.first_name()
        city = fake.city()
        lastname = fake.last_name()
        return SettingsData(name=name, lastname=lastname, email=email, city=city)