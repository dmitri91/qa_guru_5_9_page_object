from selene import browser, have

from qa_guru_page_object.users import User


class SimpleRegistrationPage:

    def registration_form(self, student: User):
        browser.element('#userName').type(student.full_name)
        browser.element('#userEmail').type(student.email)
        browser.element('#currentAddress').type(student.current_address)
        browser.element('#permanentAddress').type(student.permanent_address)
        browser.element('#submit').click()

    def should_have_registered_simplple_form(self, student: User):
        browser.all('#output p').should(have.exact_texts(
            f'Name:{student.full_name}',
            f'Email:{student.email}',
            f'Current Address :{student.current_address}',
            f'Permananet Address :{student.permanent_address}')
        )
