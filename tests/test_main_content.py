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
