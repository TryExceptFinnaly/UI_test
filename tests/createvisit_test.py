from pages.create_visit_page import CreateVisitPage
from time import sleep

class TestCreateVisit:

    def test_create_visit(self, driver):
        page = CreateVisitPage(driver, 'https://nt.ris-x.com/')
        page.open()
        page.authorization()
        entered_data = page.submit_and_fill_fields()
        sleep(5)
        data = page.check_data_page()
        print(f'Entered data: {entered_data}')
        print(f'Data: {data}')
        assert entered_data == data
