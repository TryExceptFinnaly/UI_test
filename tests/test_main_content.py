import allure

from pages.p_main_content import MainContentPage


@allure.feature('Main Content')
class TestMainContent:
    URL = 'https://nt.ris-x.com/'

    @allure.title('Open slide menu')
    def test_open_slide_menu(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.change_slide_menu(active=True)
        page.hover_all_menu(active=True)

    @allure.title('Close slide menu')
    def test_close_slide_menu(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.change_slide_menu(active=False)
        page.hover_all_menu(active=False)
        page.hover_all_menu_with_submenu()

    @allure.title('Open slide menu admin')
    def test_open_slide_menu_admin(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.switch_panel_mode('admin')
        page.change_slide_menu(active=True)
        page.hover_all_menu(active=True)

    @allure.title('Close slide menu admin')
    def test_close_slide_menu_admin(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.switch_panel_mode('admin')
        page.change_slide_menu(active=False)
        page.hover_all_menu(active=False)
        page.hover_all_menu_with_submenu()

    @allure.title('Switch style')
    def test_switch_style(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        assert page.switch_style_css('dark'), 'Dark style CSS missing in HTML'
        page.sleep(3)
        assert page.switch_style_css('white'), 'White style CSS missing in HTML'
        page.sleep(3)

    @allure.title('Switch panel mode')
    def test_switch_panel_mode(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.switch_panel_mode('admin')
        page.sleep(3)
        page.switch_panel_mode('user')
        page.sleep(3)

    @allure.title('Matching data and footer data')
    def test_matching_user_data(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        data, footer_data = page.check_user_data()
        assert data == footer_data, 'The data does not match the data footer'

    @allure.title('Switch role')
    def test_switch_role(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        roles = ['Врач', 'Эксперт', 'Врач']
        for role in roles:
            page.switch_role(role)
            data, footer_data = page.check_user_data()
            assert data == footer_data, 'The data does not match the data footer'

    @allure.title('Switch work place')
    def test_switch_work_place(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        place = 'ГБУЗ "Старая Руса", Отделение лучевой диагностики, Кабинет КТ №1'
        page.switch_work_place(place)
        data, footer_data = page.check_user_data()
        assert data == footer_data, 'The data does not match the data footer'
