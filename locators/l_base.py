from selenium.webdriver.common.by import By


class BaseLocators:
    PAGE_NOTIFICATIONS = (By.XPATH, "//div[@class='notification-message']/div[@class='message']")
    LOADING_BAR = (
        By.CSS_SELECTOR, "div[class^='Loading__loading']>div[class^='Loading__bar'][style*='display: block;']")
