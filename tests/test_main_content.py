from pages.p_main_content import MainContentPage


class TestMainContentPage:
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
