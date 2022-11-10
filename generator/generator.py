from data.data import Patient
from faker import Faker
from faker.providers.phone_number import Provider
from random import randint


class RussianPhoneNumber(Provider):
    def russian_phone_number(self):
        return f'+79{self.msisdn()[4:]}'


faker_ru = Faker('ru_RU')
faker_ru.add_provider(RussianPhoneNumber)


def write_seed():
    with open('seed', 'w', encoding='utf-8') as file:
        file.write(f'{randint(0, 1000)}')


def read_seed():
    try:
        with open('seed', 'r', encoding='utf-8') as file:
            return int(file.read())
    except Exception:
        return None


def generated_person():
    Faker.seed(read_seed())
    yield Patient(
        first_name=f'{faker_ru.first_name()}',
        last_name=f'{faker_ru.last_name()}',
        middle_name=f'{faker_ru.middle_name()}',
        email=f'{faker_ru.email()}',
        phone_number=f'{faker_ru.russian_phone_number()}',
        birthday=f'{faker_ru.date("%d.%m.%Y")}'
    )
