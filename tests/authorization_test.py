from pages.authorization_page import AuthorizationPage


class TestAuthorization:

    def test_authorization(self, driver):
        form_page = AuthorizationPage(driver, 'https://nt.ris-x.com/')
        form_page.open()
        form_page.authorization()
        user_name, study_page = form_page.check_data_page()
        assert user_name == 'Дубровин А. В.'
        assert study_page == 'Исследования'
