from qa_guru_page_object.application import app

from qa_guru_page_object.users import student


def test_simple_registration_form(web_browser):
    app.left_panel.open_simple_registration_form()

    app.simple_registration_page.registration_form(student)

    app.simple_registration_page.should_have_registered_simplple_form(student)
