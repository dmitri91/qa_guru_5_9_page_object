import os
import allure
from selene import have, command

from qa_guru_page_object.users import User
from utils import resource


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Открыть форму регистрации')
    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')
        self.browser.driver.execute_script("$('#fixedban').remove()")

    @allure.step('Заполнить форму')
    def registration(self, student: User):
        self.browser.element('#firstName').type(student.first_name)
        self.browser.element('#lastName').type(student.last_name)
        self.browser.element('#userEmail').type(student.email)
        self.browser.all('[name=gender]').element_by(have.value(student.gender.male.value)).element('..').click()
        self.browser.element('#userNumber').type(student.number)
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__year-select').type(student.birthday.year)
        self.browser.element('.react-datepicker__month-select').type(student.birthday.strftime('%B'))
        self.browser.element(f'[aria-label="Choose Wednesday, {student.birthday.strftime("%B")} '
                        f'{student.birthday.strftime("%d").lstrip("0")}th, {student.birthday.year}"]').click()
        for subject in student.subject:
            self.browser.element('#subjectsInput').type(subject.value).press_enter()
        for hobby in student.hobbies:
            self.browser.all('.custom-checkbox').element_by(have.exact_text(hobby.value)).click()
        self.browser.element('#uploadPicture').send_keys(resource.get_path(student.picture))
        self.browser.element('#currentAddress').type(student.address)
        self.browser.element('#state').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        self.browser.element('#city').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser = self.browser
        browser.driver.execute_script('$("#submit").click()')

    @allure.step('Проверить результат заполнения')
    def should_have_registered(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birthday.strftime("%d")} {student.birthday.strftime("%B")},{student.birthday.year}'
        state_and_city = f'{student.state} {student.city}'
        subject = ', '.join([subject.value for subject in student.subject])
        hobbies = ', '.join([hobby.value for hobby in student.hobbies])
        self.browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender.male.value}',
            f'Mobile {student.number}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {hobbies}',
            f'Picture {student.picture}',
            f'Address {student.address}',
            f'State and City {state_and_city}')
        )
