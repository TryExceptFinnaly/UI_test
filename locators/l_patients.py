from selenium.webdriver.common.by import By


class PatientsPageLocators:
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input#lastName")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input#firstName")
    INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "input#middleName")
    INPUT_BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
