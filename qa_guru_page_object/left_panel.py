from selene import browser, have


class LeftPanel:

    def __init__(self):
        self.elements_left_panel = browser.all('.header-wrapper>div')

    def open(self, block_name, value_list):
        browser.open('/forms')
        self.elements_left_panel.element_by(have.exact_text(block_name)).click()
        self.elements_left_panel.element_by(have.exact_text(block_name)).element('../../..').all('.element-list li')\
            .element_by(have.exact_text(value_list)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
