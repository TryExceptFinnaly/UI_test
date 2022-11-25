import requests
import selenium.common.exceptions

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

    def wait_until(self, timeout, method, return_false: bool = False):
        if return_false:
            try:
                return Wait(self.driver, timeout).until(method)
            except selenium.common.exceptions.TimeoutException:
                return False
        else:
            return Wait(self.driver, timeout).until(method)

    def element_is_visible(self, locator, scroll: bool = False, timeout: int = DEFAULT_TIMEOUT,
                           return_false: bool = False):
        if scroll:
            self.scroll_to_element(self.element_is_present(locator))
        return self.wait_until(timeout, EC.visibility_of_element_located(locator), return_false)

    def elements_are_visible(self, locator, timeout: int = DEFAULT_TIMEOUT, element: int = None,
                             return_false: bool = False):
        """Return list elements by locator\nelement(int) - return an element from a list(-1 = random)"""
        elements = self.wait_until(timeout, EC.visibility_of_all_elements_located(locator), return_false)
        if (element is not None) and elements:
            if element == -1:
                return elements[randint(0, len(elements) - 1)]
            return elements[element]
        return elements

    def element_is_present(self, locator, timeout: int = DEFAULT_TIMEOUT, return_false=False):
        return self.wait_until(timeout, EC.presence_of_element_located(locator), return_false)

    def elements_are_present(self, locator, timeout: int = DEFAULT_TIMEOUT, element: int = None, return_false=False):
        """Return list elements by locator\nelement(int) - return an element from a list(-1 = random)"""
        elements = self.wait_until(timeout, EC.presence_of_all_elements_located(locator), return_false)
        if (element is not None) and elements:
            if element == -1:
                return elements[randint(0, len(elements) - 1)]
            return elements[element]
        return elements

    def element_is_not_visible(self, locator, timeout: int = DEFAULT_TIMEOUT, return_false=False):
        return self.wait_until(timeout, EC.invisibility_of_element_located(locator), return_false)

    def element_is_clickable(self, locator, timeout: int = DEFAULT_TIMEOUT, return_false=False):
        return self.wait_until(timeout, EC.element_to_be_clickable(locator), return_false)

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def zoom_level(self, level: int):
        self.driver.execute_script(f'document.body.style.zoom="{level}%";')

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @staticmethod
    def click_and_send_keys(element, send_keys):
        element.click()
        element.send_keys(send_keys)

    @staticmethod
    def sleep(secs: int):
        sleep(secs)

    @staticmethod
    def get_request(url: str):
        return requests.get(url)

    def select_node_in_jstree(self, locator_nodes, element):
        nodes = self.elements_are_present(locator_nodes, element=element)
        nodes_i = None
        while True:
            if nodes_i:
                nodes = self.elements_are_visible(locator_nodes, element=element)
            self.scroll_to_element(nodes)
            diagnoses_mkb_class = nodes.get_attribute('class')
            diagnoses_mkb_id = nodes.get_attribute('id')
            locator_nodes = (locator_nodes[0], f'{locator_nodes[1]}[id="{diagnoses_mkb_id}"]')
            if 'jstree-leaf' in diagnoses_mkb_class:
                locator_nodes = (locator_nodes[0], f'{locator_nodes[1]}>a')
                self.element_is_visible(locator_nodes, True).click()
                break
            nodes_i = (locator_nodes[0], f'{locator_nodes[1]}>i')
            self.element_is_visible(nodes_i, True).click()
            locator_nodes = (locator_nodes[0], f'{locator_nodes[1]}>ul>li.jstree-node')
