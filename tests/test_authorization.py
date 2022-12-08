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
        page.check_user_authorization()
        assert f'{self.URL}login/' not in page.current_url()
        page.logout()
        assert f'{self.URL}login/' in page.current_url()
