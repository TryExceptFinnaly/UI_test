from pages.base_page import BasePage
from locators.form_page_locator import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        user_name = 'dav'
        user_password = 'dav'
        self.element_is_visible(Locators.USER_NAME).send_keys(user_name)
        self.element_is_visible(Locators.USER_PASSWORD).send_keys(user_password)
        self.element_is_visible(Locators.BTN_SUBMIT).click()
        return self.element_is_visible(Locators.LABEL_FIO).text