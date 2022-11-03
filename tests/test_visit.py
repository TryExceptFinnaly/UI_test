from pages.p_visit import VisitPage
from time import sleep


class TestVisit:
    class TestVisitPage:
        pass

    class TestCreateVisitPage:
        def test_create_visit(self, driver):
            page = VisitPage(driver, 'https://nt.ris-x.com/')
            page.open()
            page.authorization()
            page.go_to_create_visit()
            entered_data = page.fill_data_patient()
            page.create_visit()
            sleep(5)
            data = page.check_result_created_visit()
            print(f'Entered data: {entered_data}')
            print(f'Data: {data}')
            assert entered_data == data
