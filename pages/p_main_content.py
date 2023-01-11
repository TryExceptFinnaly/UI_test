from pages.p_authorization import AuthorizationPage
from locators.l_main_content import MainContentPageLocators as MainContentLocators
from generator.generator import generated_person, write_seed


class MainContentPage(AuthorizationPage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.patient_info = next(generated_person())

    def generate_new_patient(self, seed: int = 0):
        write_seed(seed)
        self.patient_info = next(generated_person())

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

    def switch_role(self, role):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        self.element_is_visible(MainContentLocators.PLACE_OF_WORK).click()
        current_role = self.element_is_visible(MainContentLocators.SESSION_ROLE_VALUE).text
        if role != current_role:
            self.element_is_visible(MainContentLocators.SESSION_ROLE_CONTAINER).click()
            locator = (MainContentLocators.SESSION_ROLE[0], MainContentLocators.SESSION_ROLE[1] + f'[text()="{role}"]')
            self.element_is_visible(locator).click()
        self.element_is_visible(MainContentLocators.SAVE_USER_DATA).click()
        self.waiting_for_notification('Данные сохранены.')

    def switch_work_place(self, place):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        self.element_is_visible(MainContentLocators.PLACE_OF_WORK).click()
        current_place = self.element_is_visible(MainContentLocators.SESSION_PLACE_VALUE).text
        if place != current_place:
            self.element_is_visible(MainContentLocators.SESSION_PLACE_CONTAINER).click()
            locator = (
                MainContentLocators.SESSION_PLACE[0], MainContentLocators.SESSION_PLACE[1] + f'[text()="{place}"]')
            self.element_is_visible(locator).click()
        self.element_is_visible(MainContentLocators.SAVE_USER_DATA).click()
        self.waiting_for_notification('Данные сохранены.')

    def get_footer_user_data(self):
        """return: role, (mo, department, room)"""
        footer_data = self.element_is_visible(MainContentLocators.USER_DATA_FOOTER)
        footer_role = self.element_child_nodes_text(footer_data, 0)
        footer_mo = self.element_child_nodes_text(footer_data, 2)
        footer_department = self.element_child_nodes_text(footer_data, 4)
        footer_room = self.element_child_nodes_text(footer_data, 6)
        return footer_role, (footer_mo, footer_department, footer_room)

    def check_user_data(self):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        self.element_is_visible(MainContentLocators.PLACE_OF_WORK).click()
        role = self.element_is_visible(MainContentLocators.SESSION_ROLE_VALUE).text
        place = self.element_is_visible(MainContentLocators.SESSION_PLACE_VALUE).text
        self.element_is_visible(MainContentLocators.SAVE_USER_DATA).click()
        footer_role, footer_place = self.get_footer_user_data()
        footer_place = f'{footer_place[0]}, {footer_place[1]}, {footer_place[2]}'
        return (role, place), (footer_role, footer_place)
