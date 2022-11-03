from pages.p_authorization import AuthorizationPage


class TestAuthorization:
    class TestAuthorizationPage:
        def test_authorization(self, driver):
            page = AuthorizationPage(driver, 'https://nt.ris-x.com/')
            page.open()
            page.authorization()
            user_name, study_page = page.check_result_authorization()
            assert user_name == 'Дубровин А. В.'
            assert study_page == 'Исследования'
