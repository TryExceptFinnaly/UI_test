from dataclasses import dataclass


@dataclass
class Patient:
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    sex: str = None
    email: str = None
    phone_number: str = None
    birth_year: str = None
    birth_month: str = None
    birth_day: str = None
