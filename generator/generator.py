from data.data import Patient
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Patient(
        full_name=f'{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}',
        email=f'{faker_ru.email()}',
        phone_number=f'{faker_ru.phone_number()}',
    )
