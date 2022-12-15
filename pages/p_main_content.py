from pages.p_authorization import AuthorizationPage
from locators.l_main_content import MainContentPageLocators as MainContentLocators


class MainContentPage(AuthorizationPage):
    def change_slide_menu(self, active=False):
        slide_menu_btn = self.element_is_visible(MainContentLocators.SLIDE_MENU_BTN)
        slide_menu_btn_class = slide_menu_btn.get_attribute('class')
        if 'is-active' in slide_menu_btn_class:
            if not active:
                slide_menu_btn.click()
        else:
            if active:
                slide_menu_btn.click()

    def hover_all_menu(self, active=False):
        if active:
            items = self.elements_are_visible(MainContentLocators.SLIDE_MENU_ALL_ITEMS)
        else:
            items = self.elements_are_visible(MainContentLocators.SLIDE_MENU_MAIN_ITEMS)
        for item in items:
            self.action_move_to_element(item)
            print(item.text)

    def hover_all_menu_with_submenu(self):
        items = self.elements_are_visible(MainContentLocators.SLIDE_MENU_SUB_ITEMS)
        for idx in range(len(items)):
            self.action_move_to_element(items[idx])
            sub_items = self.elements_are_visible((MainContentLocators.SLIDE_MENU_SUB_ITEMS[0],
                                                   f'({MainContentLocators.SLIDE_MENU_SUB_ITEMS[1]})[{idx + 1}]/ul/li/a'))
            for sub_item in sub_items:
                self.action_move_to_element(sub_item)
                print(sub_item.text)

    def switch_style_css(self, style: str = 'dark'):
        css_theme = self.element_is_present(MainContentLocators.CURRENT_STYLE).get_attribute('href')
        if style in css_theme:
            return True
        else:
            self.element_is_visible(MainContentLocators.SWITCH_STYLE).click()
            css_theme = self.element_is_present(MainContentLocators.CURRENT_STYLE).get_attribute('href')
            return True if style in css_theme else False

    def switch_panel_mode(self, switch_mode: str):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        match switch_mode:
            case 'admin':
                switch_mode = 'logo-admin.png'
                locator = MainContentLocators.SWITCH_ADMIN_MODE
            case 'user':
                switch_mode = 'logo.png'
                locator = MainContentLocators.SWITCH_USER_MODE
            case _:
                return 'Incorrect switch_mode'
        if switch_mode not in self.element_is_visible(MainContentLocators.LOGO).get_attribute('src'):
            self.element_is_visible(locator).click()
