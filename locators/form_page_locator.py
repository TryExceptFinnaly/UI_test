from selenium.webdriver.common.by import By


class FormPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#username')
    USER_PASSWORD = (By.CSS_SELECTOR, '#password')
    BTN_SUBMIT = (By.TAG_NAME, 'button')
    LABEL_FIO = (
        By.CSS_SELECTOR,
        '#app > div.wrap > div.header > div > div > ul.nav.navbar-nav.pull-right > li.dropdown > div > div.pull-right > div:nth-child(1)'
    )
    STUDY_PAGE = (By.TAG_NAME, 'h1')
    PLANNED_PAGE = (By.CSS_SELECTOR, "#slide-menu>div>ul>li>a[href='/planned/']")
