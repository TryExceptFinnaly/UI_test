from data.data import Patient
from faker import Faker
from faker.providers.phone_number import Provider


class RussianPhoneNumber(Provider):
    def russian_phone_number(self):
        return f'+79{self.msisdn()[4:]}'


faker_ru = Faker('ru_RU')
Faker.seed()
faker_ru.add_provider(RussianPhoneNumber)


def generated_person():
    yield Patient(
        first_name=f'{faker_ru.first_name()}',
        last_name=f'{faker_ru.last_name()}',
        middle_name=f'{faker_ru.middle_name()}',
        email=f'{faker_ru.email()}',
        phone_number=f'{faker_ru.russian_phone_number()}',
        birthday=f'{faker_ru.date("%d-%m-%Y")}',
    )
