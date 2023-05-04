from qa_guru_page_object.registration_page import RegistrationPage


def test_filling_form(web_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Dmitii')
    registration_page.fill_last_name('Larin')
    registration_page.fill_email('Dmitrii@mail.ru')
    registration_page.choose_user_gender('Male')
    registration_page.fill_number('79290423322')
    registration_page.fill_date_of_birth('1991', 'January', '9')
    registration_page.fill_subjects('Arts')
    registration_page.choose_hobbies('Sports')
    registration_page.download_picture('cat.png')
    registration_page.fill_current_address('Moscow are')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Lucknow')
    registration_page.submit()
    # THEN
    registration_page.should_have_registered('Dmitii Larin', 'Dmitrii@mail.ru', 'Male',
                                             '7929042332', '09 January,1991',
                                             'Arts', 'Sports', 'cat.png',
                                             'Moscow are', 'Uttar Pradesh Lucknow')
