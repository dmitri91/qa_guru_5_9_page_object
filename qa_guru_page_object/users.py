from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    arts = 'Arts'
    maths = 'Maths'
    biology = 'Biology'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    full_name: str
    email: str
    gender: Gender
    number: str
    birthday: date
    subject: List[Subject]
    hobbies: List[Hobby]
    picture: str
    current_address: str
    permanent_address: str
    state: str
    city: str


student = User(
    first_name='Dmitii',
    last_name='Larin',
    full_name='Dmitii Larin',
    email='Dmitrii@mail.ru',
    gender=Gender.male,
    number='7929042332',
    birthday=date(1991, 1, 9),
    subject=[Subject.arts],
    hobbies=[Hobby.music, Hobby.sports],
    picture='cat.png',
    current_address='Moscow are',
    permanent_address='RF',
    state='Uttar Pradesh',
    city='Lucknow')
