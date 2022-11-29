from pages.p_authorization import AuthorizationPage


class TestAuthorizationPage:
    URL = 'https://nt.ris-x.com/'

    def test_authorization(self, driver):
        page = AuthorizationPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_user_authorization()
        assert 'https://nt.ris-x.com/login/' not in page.current_url()
        page.logout()
        assert 'https://nt.ris-x.com/login/' in page.current_url()
