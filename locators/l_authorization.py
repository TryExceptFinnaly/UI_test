from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input#username')
    USER_PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BTN_SUBMIT = (By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    LABEL_FIO = (By.CSS_SELECTOR, 'div.menu-item-user>div.pull-right>div:nth-child(1)')
    STUDY_PAGE = (By.CSS_SELECTOR, 'div.pull-left>h1.pull-left')