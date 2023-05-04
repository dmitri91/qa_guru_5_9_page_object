from qa_guru_page_object.registration_page import RegistrationPage
from qa_guru_page_object.users import student


def test_filling_form(web_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.registration(student)

    registration_page.should_have_registered(student)
