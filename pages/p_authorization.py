from pages.p_base import BasePage
from locators.l_authorization import AuthorizationPageLocators as AuthorizationLocators
from locators.l_main_content import MainContentPageLocators as MainContentLocators
from locators.l_base import BaseLocators


class AuthorizationPage(BasePage):
    Locators = BaseLocators()

    # def __init__(self, driver, url):
    #     super().__init__(driver, url)
    #     self.user = 'dav'
    #     self.password = 'dav'

    def authorization(self, user: str = 'dav', password: str = 'dav'):
        self.element_is_visible(AuthorizationLocators.USER_NAME).send_keys(user)
        self.element_is_visible(AuthorizationLocators.USER_PASSWORD).send_keys(password)
        self.element_is_visible(AuthorizationLocators.BTN_SUBMIT).click()
        self.element_is_not_visible(self.Locators.LOADING_BAR)

    def check_alert_message(self):
        return self.element_is_visible(AuthorizationLocators.ALERT_MSG).text

    def waiting_for_notification(self, waiting_notification: str, return_false: bool = False):
        locator_notification = (
            self.Locators.PAGE_NOTIFICATIONS[0],
            f"{self.Locators.PAGE_NOTIFICATIONS[1]}[text()='{waiting_notification}']")
        return self.element_is_visible(locator_notification, scroll=False, return_false=return_false)

    def logout(self):
        self.element_is_visible(MainContentLocators.BTN_LOGOUT).click()
        self.element_is_not_visible(self.Locators.LOADING_BAR)
