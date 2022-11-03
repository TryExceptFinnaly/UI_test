from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input#username')
    USER_PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BTN_SUBMIT = (By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    LABEL_FIO = (By.CSS_SELECTOR, 'div.pull-right>div:nth-child(1)')
    STUDY_PAGE = (By.CSS_SELECTOR, 'div.pull-left>h1.pull-left')


class VisitPageLocators:
    CREATE_VISIT = (By.CSS_SELECTOR, "a.btn.btn-primary[href='/visit/create/']")
    FULL_NAME = (By.CSS_SELECTOR, "input#full_name")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input#phone_number")
    EMAIL = (By.CSS_SELECTOR, "input#email")
    BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
    SEX_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div")
    SEX = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div div[tabindex='-1']")
    TYPES_OF_STUDY_CONTAINER = (
    By.CSS_SELECTOR, "label.control-label[for='studies']+div.studies-field>span div.react-select__control")
    TYPE_OF_STUDY = (By.CSS_SELECTOR, "label.control-label[for='studies']+div div[tabindex='-1']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>div.btn-toolbar[role='toolbar']>div>button.btn.btn-primary")
    PATIENTS_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>a[href^='/share/visits/']")
    PATIENTS_BIRTHDAY_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>span:has(br)")
    REFRESH_STUDY_PAGE = (By.CSS_SELECTOR, "i.fa.fa-refresh")
    BLOCK_PAGE = (By.CSS_SELECTOR, "div[role='dialog']")
