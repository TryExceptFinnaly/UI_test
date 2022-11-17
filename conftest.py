import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size="1920,1080"')
    return options


@pytest.fixture(scope='function') 
def driver(chrome_options):
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    yield driver
    driver.quit()
