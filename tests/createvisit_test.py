from time import sleep
from pages.create_visit_page import CreateVisitPage


class TestCreateVisit:

    def test_create_visit(self, driver):
        form_page = CreateVisitPage(driver, 'https://nt.ris-x.com/')
        form_page.open()
        form_page.authorization()
        form_page.submit_and_fill_fields()
        sleep(10)
