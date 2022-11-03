from pages.p_base import BasePage
from locators.l_visit import AuthorizationPageLocators as Locators


class AuthorizationPage(BasePage):

    def authorization(self):
        self.element_is_visible(Locators.USER_NAME).send_keys(self.user)
        self.element_is_visible(Locators.USER_PASSWORD).send_keys(self.password)
        self.element_is_visible(Locators.BTN_SUBMIT).click()

    def check_result_authorization(self):
        label_fio = self.element_is_present(Locators.LABEL_FIO).text
        study_page = self.element_is_present(Locators.STUDY_PAGE).text
        return label_fio, study_page
