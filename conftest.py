import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('incognito')
    options.add_argument('start-maximized')
    # options.add_argument('flag-switches-begin')
    # options.add_argument('flag-switches-end')
    # options.add_argument('user-data-dir=C:\\Users\\LINS\\AppData\\Local\\Google\\Chrome\\User Data')
    # options.add_argument('profile-directory=Default')
    # print(os.path.dirname(__file__))
    # options.add_extension('extensions/1.2.13_0.crx')
    # options.add_argument('--window-size="1920,1080"')
    return options


@pytest.fixture()
def driver(chrome_options):
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    yield driver
    driver.quit()
