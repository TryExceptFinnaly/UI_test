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
    person = faker_ru.simple_profile()
    person_name = person['name'].split()

    yield Patient(
        first_name=f'{person_name[0]}',
        last_name=f'{person_name[1]}',
        middle_name=f'{person_name[2]}',
        sex=f'{person["sex"]}',
        email=f'{person["mail"]}',
        phone_number=f'{faker_ru.russian_phone_number()}',
        birth_year=f'{person["birthdate"].year}',
        birth_month=f'{person["birthdate"].month:02}',
        birth_day=f'{person["birthdate"].day:02}',
    )
