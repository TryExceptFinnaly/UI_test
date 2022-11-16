from selenium.webdriver.common.by import By


class PatientsPageLocators:
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input#lastName")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input#firstName")
    INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "input#middleName")
    INPUT_BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
    TBODY_PATIENTS = (By.CSS_SELECTOR, "table.table.table-bordered.table-condensed>tbody")
    PATIENT = (By.CSS_SELECTOR, "table.table.table-bordered.table-condensed>tbody>tr:nth-child(1)>td")