from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    CREATE_VISIT = (By.CSS_SELECTOR, "div>a[href='/visit/create/']")
    FULL_NAME = (By.CSS_SELECTOR, "div>input[id='full_name']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "div>input[id='phone_number']")
    EMAIL = (By.CSS_SELECTOR, "div>input[id='email']")
