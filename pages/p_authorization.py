from pages.p_base import BasePage
from locators.l_authorization import AuthorizationPageLocators as AuthorizationLocators
from locators.l_main_content import MainContentPageLocators as MainContentLocators
from locators.l_base import BaseLocators


class AuthorizationPage(BasePage):
    Locators = BaseLocators()

    def authorization(self):
        self.element_is_visible(AuthorizationLocators.USER_NAME).send_keys(self.user)
        self.element_is_visible(AuthorizationLocators.USER_PASSWORD).send_keys(self.password)
        self.element_is_visible(AuthorizationLocators.BTN_SUBMIT).click()

    def check_result_authorization(self):
        return self.element_is_visible(MainContentLocators.LABEL_FIO).text

    def waiting_for_notification(self, waiting_notification: str, return_false: bool = False):
        locator_notification = (
            self.Locators.PAGE_NOTIFICATIONS[0],
            f"{self.Locators.PAGE_NOTIFICATIONS[1]}[text()='{waiting_notification}']")
        return self.element_is_visible(locator_notification, scroll=False, return_false=return_false)

    def logout(self):
        self.element_is_visible(MainContentLocators.BTN_LOGOUT).click()
