from pages.authorization_page import AuthorizationPage


class TestAuthorization:

    def test_authorization(self, driver):
        page = AuthorizationPage(driver, 'https://nt.ris-x.com/')
        page.open()
        page.authorization()
        user_name, study_page = page.check_data_page()
        assert user_name == 'Дубровин А. В.'
        assert study_page == 'Исследования'
