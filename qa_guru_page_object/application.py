from qa_guru_page_object.left_panel import LeftPanel
from qa_guru_page_object.registration_page import RegistrationPage
from qa_guru_page_object.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.left_panel = LeftPanel()
        self.simple_registration_page = SimpleRegistrationPage()


app = Application()