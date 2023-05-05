from qa_guru_page_object.application import app
from qa_guru_page_object.users import student


def test_filling_form(web_browser):
    app.registration_page.open()

    app.registration_page.registration(student)

    app.registration_page.should_have_registered(student)
