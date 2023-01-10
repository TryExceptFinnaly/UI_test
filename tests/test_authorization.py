import allure

from pages.p_authorization import AuthorizationPage


@allure.feature('Authorization')
class TestAuthorization:
    URL = 'https://nt.ris-x.com/'

    @allure.title('Check authorization and logout')
    def test_authorization_and_logout(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization()
        assert f'{self.URL}login/' not in page.current_url(), 'Authorization: Incorrect current URL'
        page.logout()
        assert f'{self.URL}login/' in page.current_url(), 'Logout: Incorrect current URL'

    @allure.title('Check incorrect user authorization')
    def test_incorrect_user_authorization(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization(user='kov')
        assert f'{self.URL}login/' in page.current_url(), 'Authorization: Incorrect current URL'
        assert 'Невозможно войти с предоставленными учетными данными.' == page.check_alert_message()

    @allure.title('Check incorrect password authorization')
    def test_incorrect_password_authorization(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization(password='kov')
        assert f'{self.URL}login/' in page.current_url(), 'Authorization: Incorrect current URL'
        assert 'Невозможно войти с предоставленными учетными данными.' == page.check_alert_message()

    @allure.title('Check incorrect password authorization')
    def test_empty_form_authorization(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization(user='', password='')
        assert f'{self.URL}login/' in page.current_url(), 'Authorization: Incorrect current URL'
        assert 'Форма заполнена с ошибками.' == page.check_alert_message()
