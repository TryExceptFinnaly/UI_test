from dataclasses import dataclass


@dataclass
class Patient:
    full_name: str = None
    email: str = None
    phone_number: str = None
    birthday: str = None
