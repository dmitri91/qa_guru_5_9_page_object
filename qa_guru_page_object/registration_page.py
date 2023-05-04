import os

from selene import browser, have

from qa_guru_page_object.users import User


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def registration(self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.all('[name=gender]').element_by(have.value(student.gender.male.value)).element('..').click()
        browser.element('#userNumber').type(student.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(student.birthday.year)
        browser.element('.react-datepicker__month-select').type(student.birthday.strftime('%B'))
        browser.element(f'[aria-label="Choose Wednesday, {student.birthday.strftime("%B")} '
                        f'{student.birthday.strftime("%d").lstrip("0")}th, {student.birthday.year}"]').click()
        for subject in student.subject:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        for hobby in student.hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby.value)).click()
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/{student.picture}")
        browser.element('#currentAddress').type(student.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser.element('#submit').execute_script('element.click()')

    def should_have_registered(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birthday.strftime("%d")} {student.birthday.strftime("%B")},{student.birthday.year}'
        state_and_city = f'{student.state} {student.city}'
        subject = ', '.join([subject.value for subject in student.subject])
        hobbies = ', '.join([hobby.value for hobby in student.hobbies])
        browser.all('tbody tr').should(have.exact_texts(
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
