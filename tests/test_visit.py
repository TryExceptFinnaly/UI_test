from pages.p_visit import VisitPage, CreateVisitPage, ComparisonVisitPage, CreateProtocolPage


class TestVisitPage:
    URL = 'https://nt.ris-x.com/visit/'

    def test_refresh_page(self, driver):
        page = VisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.refresh_study_page()


class TestCreateVisitPage:
    URL = 'https://nt.ris-x.com/visit/'
    entered_data = ''

    def test_create_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        TestCreateVisitPage.entered_data = page.fill_base_fields_patient()
        page.fill_params_fields_patient()
        page.fill_additional_fields_patient()
        page.fill_passport_registration_fields_patient()
        page.save_visit()
        page.waiting_for_notification('Данные сохранены.')
        print(f'Entered data: {TestCreateVisitPage.entered_data}')

    def test_check_created_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        data = page.check_result_created_visit()
        print(f'Data: {data}')
        assert TestCreateVisitPage.entered_data == data

    def test_delete_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_created_visit()
        page.delete_visit()
        page.sleep(5)


class TestComparisonVisitPage:
    URL = 'https://nt.ris-x.com/visit/'

    def test_compare_created_visit(self, driver):
        page = ComparisonVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_created_visit()
        page.save_and_bind_visit()
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.compare_visit()


class TestCreateProtocolPage:
    URL = 'https://nt.ris-x.com/visit/'

    def test_create_protocol_on_created_visit(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol()
        page.save_protocol()
        page.waiting_for_notification('Данные сохранены.')
