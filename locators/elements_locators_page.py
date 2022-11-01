from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#username')
    USER_PASSWORD = (By.CSS_SELECTOR, '#password')
    BTN_SUBMIT = (By.TAG_NAME, 'button')
    LABEL_FIO = (
        By.CSS_SELECTOR,
        '#app > div.wrap > div.header > div > div > ul.nav.navbar-nav.pull-right > li.dropdown > div > div.pull-right > div:nth-child(1)'
    )
    STUDY_PAGE = (By.TAG_NAME, 'h1')


class CreateVisitPageLocators:
    CREATE_VISIT = (By.CSS_SELECTOR, "div>a[href='/visit/create/']")
    FULL_NAME = (By.CSS_SELECTOR, "div>input[id='full_name']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "div>input[id='phone_number']")
    EMAIL = (By.CSS_SELECTOR, "div>input[id='email']")
    BIRTHDAY = (By.CSS_SELECTOR, "div>input[id='birth']")
    GENDER_CONTAINER = (By.XPATH, r'//*[@id="regform-tabs-pane-base"]/div/div[1]/div[4]/div[2]/div/div')
    GENDER = (By.CSS_SELECTOR, "div[id*='react-select-'][id*='-option-']")
    TYPES_OF_STUDY_CONTAINER = (By.XPATH, r'//*[@id="regform-tabs-pane-base"]/div/div[3]/div[2]/div/span/div/div')
    TYPES_OF_STUDY = (By.CSS_SELECTOR, "div[id*='react-select-'][id*='-option-']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-primary']")

