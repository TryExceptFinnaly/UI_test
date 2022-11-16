from pages.p_base import BasePage
from locators.l_authorization import AuthorizationPageLocators as AuthorizationLocators
from locators.l_visit import VisitPageLocators as VisitLocators


class AuthorizationPage(BasePage):

    def authorization(self):
        self.element_is_visible(AuthorizationLocators.USER_NAME).send_keys(self.user)
        self.element_is_visible(AuthorizationLocators.USER_PASSWORD).send_keys(self.password)
        self.element_is_visible(AuthorizationLocators.BTN_SUBMIT).click()

    def check_result_authorization(self):
        label_fio = self.element_is_present(VisitLocators.LABEL_FIO).text
        study_page = self.element_is_present(VisitLocators.STUDY_PAGE).text
        return label_fio, study_page
