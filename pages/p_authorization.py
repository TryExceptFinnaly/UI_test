from pages.p_base import BasePage
from locators.l_authorization import AuthorizationPageLocators as AuthorizationLocators
from locators.l_visit import VisitPageLocators as VisitLocators
from locators.l_main_content import MainContentPageLocators as MainContentLocators
from locators.l_base import BaseLocators


class AuthorizationPage(BasePage):
    Locators = BaseLocators()

    def authorization(self):
        self.element_is_visible(AuthorizationLocators.USER_NAME).send_keys(self.user)
        self.element_is_visible(AuthorizationLocators.USER_PASSWORD).send_keys(self.password)
        self.element_is_visible(AuthorizationLocators.BTN_SUBMIT).click()

    def check_result_authorization(self):
        label_fio = self.element_is_present(MainContentLocators.LABEL_FIO).text
        study_page = self.element_is_present(VisitLocators.STUDY_PAGE).text
        return label_fio, study_page

    def waiting_for_notification(self, waiting_notification: str, return_false: bool = False):
        locator_notification = (
        BaseLocators.PAGE_NOTIFICATIONS[0], f"{BaseLocators.PAGE_NOTIFICATIONS[1]}[text()='{waiting_notification}']")
        return self.element_is_visible(locator_notification, return_false=return_false)
