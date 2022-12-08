from data.data import Patient, SystemDirectory
from faker import Faker
from faker.providers import DynamicProvider
from faker.providers.phone_number import Provider
from random import randint


class RussianPhoneNumber(Provider):
    def russian_phone_number(self):
        return f'+79{self.msisdn()[4:]}'


allergy_type_provider = DynamicProvider(
    provider_name='allergy_type',
    elements=list(SystemDirectory.allergy_type.keys())
)

is_cito_provider = DynamicProvider(
    provider_name='is_cito',
    elements=list(SystemDirectory.is_cito.keys())
)

identifier_type_provider = DynamicProvider(
    provider_name='identifier_type',
    elements=list(SystemDirectory.identifier_type.keys())
)

treatment_case_provider = DynamicProvider(
    provider_name='treatment_case',
    elements=list(SystemDirectory.treatment_case.keys())
)

patient_class_provider = DynamicProvider(
    provider_name='patient_class',
    elements=list(SystemDirectory.patient_class.keys())
)

insurance_company_provider = DynamicProvider(
    provider_name='insurance_company',
    elements=list(SystemDirectory.insurance_company.keys())
)

faker_ru = Faker('ru_RU')
faker_ru.add_provider(RussianPhoneNumber)
faker_ru.add_provider(allergy_type_provider)
faker_ru.add_provider(is_cito_provider)
faker_ru.add_provider(identifier_type_provider)
faker_ru.add_provider(treatment_case_provider)
faker_ru.add_provider(patient_class_provider)
faker_ru.add_provider(insurance_company_provider)


def write_seed():
    with open(r'C:\Users\kov\PycharmProjects\UI_test\tests\seed', 'w', encoding='utf-8') as file:
        file.write(f'{randint(0, 1000)}')


def read_seed():
    try:
        with open(r'C:\Users\kov\PycharmProjects\UI_test\tests\seed', 'r', encoding='utf-8') as file:
            return int(file.read())
    except FileNotFoundError:
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
        is_cito=f'{faker_ru.is_cito()}',
        allergy_type=f'{faker_ru.allergy_type()}',
        identifier_type=f'{faker_ru.identifier_type()}',
        treatment_case=f'{faker_ru.treatment_case()}',
        patient_class=f'{faker_ru.patient_class()}',
        insurance_company=f'{faker_ru.insurance_company()}'
    )
