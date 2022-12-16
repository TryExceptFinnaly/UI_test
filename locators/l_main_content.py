from selenium.webdriver.common.by import By


class MainContentPageLocators:
    USER = (By.XPATH, "//div[@class='pull-right']/div[not(@class)]")
    PLACE_OF_WORK = (By.XPATH, "//div[@class='pull-right']/div[@class='']")
    SESSION_ROLE_CONTAINER = (By.XPATH,
                              "//div[@class='pull-right']//div[label[@for='sessionRole']]/div[contains(@class,'react-select-container')]")
    SESSION_ROLE = (By.XPATH,
                    "//div[@class='pull-right']//div[label[@for='sessionRole']]/div[contains(@class,'react-select-container')]//div[contains(@class,'react-select__option')][@tabindex='-1']")
    SESSION_ROLE_VALUE = (By.XPATH,
                          "//div[@class='pull-right']//div[label[@for='sessionRole']]/div[contains(@class,'react-select-container')]//div[contains(@class,'react-select__single-value')]")
    SESSION_PLACE_CONTAINER = (By.XPATH,
                               "//div[@class='pull-right']//div[label[@for='sessionPlace']]/div[contains(@class,'react-select-container')]")
    SESSION_PLACE = (By.XPATH,
                     "//div[@class='pull-right']//div[label[@for='sessionPlace']]/div[contains(@class,'react-select-container')]//div[contains(@class,'react-select__option')][@tabindex='-1']")
    SESSION_PLACE_VALUE = (By.XPATH,
                           "//div[@class='pull-right']//div[label[@for='sessionPlace']]/div[contains(@class,'react-select-container')]//div[contains(@class,'react-select__single-value')]")
    SAVE_USER_DATA = (By.XPATH, "//div[@class='pull-right']/div//div/a[@class='btn btn-primary btn-block']")
    USER_DATA_FOOTER = (By.XPATH, "//div[@class='footer']/div[@class='container-fluid']/p")
    SLIDE_MENU_BTN = (By.CSS_SELECTOR, 'a#slide-menu-btn')
    SLIDE_MENU_OPEN = (By.CSS_SELECTOR, 'div#slide-menu.slide-menu-open')
    SLIDE_MENU_CLOSE = (By.CSS_SELECTOR, 'div#slide-menu.slide-menu-close')
    SLIDE_MENU_ALL_ITEMS = (By.CSS_SELECTOR, 'div#slide-menu>div.slide-menu-col ul li:not(.divider)>a')
    SLIDE_MENU_MAIN_ITEMS = (By.CSS_SELECTOR, 'div#slide-menu>div.slide-menu-col>ul>li:not(.divider)>a')
    SLIDE_MENU_SUB_ITEMS = (By.XPATH, '//div[@id="slide-menu"]//ul[@class="submenu"]/..')
    BTN_LOGOUT = (By.XPATH, '//i[@class="fa fa-power-off"]/../../..')
    CURRENT_STYLE = (By.CSS_SELECTOR, 'body>div#app>link')
    SWITCH_STYLE = (By.CSS_SELECTOR, 'div.pull-right>div.checkbox-switch')
    LOGO = (By.XPATH, "//img[@class='hidden-xs']")
    SWITCH_USER_MODE = (By.XPATH, "//div[@class='main-container']//i[@class='fa fa fa-user']")
    SWITCH_ADMIN_MODE = (By.XPATH, "//div[@class='main-container']//i[@class='fa fa-wrench']")
