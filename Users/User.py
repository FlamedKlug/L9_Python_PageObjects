from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    Male = '[for=gender-radio-1]'
    Female = '[for=gender-radio-2]'
    Other = '[for=gender-radio-3]'


class Hobbies(Enum):
    Sports = '[for="hobbies-checkbox-1"]'
    Reading = '[for="hobbies-checkbox-2"]'
    Music = '[for="hobbies-checkbox-3"]'


@dataclass
class User:
    first_name: str
    second_name: str
    email: str
    gender: Gender
    mobile: int
    date_of_birth: date
    subject: str
    hobbies: [Hobbies]
    picture: str
    current_address: str
    state: str
    city: str
