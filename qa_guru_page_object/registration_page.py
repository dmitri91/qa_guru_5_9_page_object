import os

from selene import browser, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_user_gender(self, text):
        browser.all('[name=gender]').element_by(have.value(text)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'[aria-label="Choose Wednesday, {month} {day}th, {year}"]').click()

    def fill_subjects(self, *args):
        for subject in args:
            browser.element('#subjectsInput').type(subject).press_enter()

    def choose_hobbies(self, *args):
        for hobby in args:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def download_picture(self, picture):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/{picture}")

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').execute_script('element.click()')

    def should_have_registered(self, full_name, email, gender, number, birthday, subject,
                               hobby, picture, current_address, state_and_city):
        browser.all('tbody tr') .should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {email}',
            f'Gender {gender}',
            f'Mobile {number}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {hobby}',
            f'Picture {picture}',
            f'Address {current_address}',
            f'State and City {state_and_city}')
        )
