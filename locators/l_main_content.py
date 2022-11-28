from selenium.webdriver.common.by import By


class MainContentPageLocators:
    LABEL_FIO = (By.CSS_SELECTOR, 'div.menu-item-user>div.pull-right>div:nth-child(1)')
    SLIDE_MENU_BTN = (By.CSS_SELECTOR, 'a#slide-menu-btn')
    SLIDE_MENU_OPEN = (By.CSS_SELECTOR, 'div#slide-menu.slide-menu-open')
    SLIDE_MENU_CLOSE = (By.CSS_SELECTOR, 'div#slide-menu.slide-menu-close')
    SLIDE_MENU_ALL_ITEMS = (By.CSS_SELECTOR, 'div#slide-menu>div.slide-menu-col ul li:not(.divider)>a')
    SLIDE_MENU_MAIN_ITEMS = (By.CSS_SELECTOR, 'div#slide-menu>div.slide-menu-col>ul>li:not(.divider)>a')
    SLIDE_MENU_SUB_ITEMS = (By.XPATH, '//div[@id="slide-menu"]//ul[@class="submenu"]/..')
    BTN_LOGOUT = (By.CSS_SELECTOR, '//i[@class="fa fa-power-off"]/../../..')