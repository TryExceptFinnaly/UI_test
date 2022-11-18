from pages.p_base import BasePage
from locators.l_authorization import AuthorizationPageLocators as AuthorizationLocators
from locators.l_visit import VisitPageLocators as VisitLocators
from locators.l_base import BaseLocators


class AuthorizationPage(BasePage):
    Locators = BaseLocators()

    def authorization(self):
        self.element_is_visible(AuthorizationLocators.USER_NAME).send_keys(self.user)
        self.element_is_visible(AuthorizationLocators.USER_PASSWORD).send_keys(self.password)
        self.element_is_visible(AuthorizationLocators.BTN_SUBMIT).click()

    def check_result_authorization(self):
        label_fio = self.element_is_present(VisitLocators.LABEL_FIO).text
        study_page = self.element_is_present(VisitLocators.STUDY_PAGE).text
        return label_fio, study_page

    def waiting_for_notification(self, waiting_notification: str):
        current_notification = ''
        while current_notification != waiting_notification:
            notifications = self.elements_are_visible(self.Locators.PAGE_NOTIFICATIONS)
            for n in notifications:
                current_notification = n.text
                if current_notification == waiting_notification:
                    break
