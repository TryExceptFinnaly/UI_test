from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from time import sleep


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.user = 'dav'
        self.password = 'dav'

    def open(self):
        self.driver.get(self.url)

    def current_url(self):
        return self.driver.current_url

    def element_is_visible(self, locator, scroll=False, timeout=DEFAULT_TIMEOUT):
        if scroll:
            self.scroll_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=DEFAULT_TIMEOUT, random_element=False):
        elements = Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        if random_element:
            return elements[randint(0, len(elements) - 1)]
        return elements

    def element_is_present(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def zoom_level(self, level):
        self.driver.execute_script(f'document.body.style.zoom="{level}%";')

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @staticmethod
    def click_and_send_keys(element, send_keys):
        element.click()
        element.send_keys(send_keys)

    @staticmethod
    def sleep(secs):
        sleep(secs)
