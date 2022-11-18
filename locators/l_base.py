from selenium.webdriver.common.by import By


class BaseLocators:
    PAGE_NOTIFICATIONS = (By.CSS_SELECTOR, 'div.notification.notification-success>div.notification-message>div.message')
