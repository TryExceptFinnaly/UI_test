from selenium.webdriver.common.by import By


class BaseLocators:
    PAGE_NOTIFICATIONS = (By.XPATH, "//div[@class='notification-message']/div[@class='message']")
