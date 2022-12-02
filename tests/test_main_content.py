from pages.p_main_content import MainContentPage


class TestMainContent:
    URL = 'https://nt.ris-x.com/'

    def test_open_slide_menu(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.change_slide_menu(active=True)
        page.hover_all_menu(active=True)

    def test_close_slide_menu(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        page.change_slide_menu(active=False)
        page.hover_all_menu(active=False)
        page.hover_all_menu_with_submenu()

    def test_switch_style(self, driver):
        page = MainContentPage(driver, self.URL)
        page.open()
        page.authorization()
        assert page.switch_style_css('dark')
        page.sleep(3)
        assert page.switch_style_css('white')
        page.sleep(3)
