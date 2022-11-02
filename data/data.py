from dataclasses import dataclass


@dataclass
class Patient:
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    email: str = None
    phone_number: str = None
    birthday: str = None
