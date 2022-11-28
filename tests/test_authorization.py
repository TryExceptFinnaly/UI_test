from pages.p_authorization import AuthorizationPage


class TestAuthorizationPage:
    URL = 'https://nt.ris-x.com/'

    def test_authorization(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization()
        user_name = page.check_result_authorization()
        assert user_name == 'Дубровин А. В.'
        page.logout()
        page.sleep(5)
