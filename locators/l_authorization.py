from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input#username')
    USER_PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BTN_SUBMIT = (By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
