from pages.p_visit import VisitPage, CreateVisitPage, BindVisitPage, CreateProtocolPage, ProtocolPage


class TestVisit:
    URL = 'https://nt.ris-x.com/visit/'

    def test_refresh_page(self, driver):
        page = VisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.refresh_study_page()


class TestCreateVisit:
    URL = 'https://nt.ris-x.com/visit/'
    entered_data = ''

    def test_create_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        TestCreateVisit.entered_data = page.fill_base_fields_patient()
        page.fill_params_fields_patient()
        page.fill_additional_fields_patient()
        page.fill_passport_registration_fields_patient()
        page.save_visit()
        page.waiting_for_notification('Данные сохранены.')
        print(f'Entered data: {TestCreateVisit.entered_data}')

    def test_check_created_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        data = page.check_result_created_visit()
        print(f'Data: {data}')
        assert TestCreateVisit.entered_data == data

    def test_delete_protocol(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_created_visit()
        page.delete_protocol()

    def test_delete_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_created_visit()
        page.delete_visit()


class TestBindVisit:
    URL = 'https://nt.ris-x.com/visit/'

    def test_bind_created_visit(self, driver):
        page = BindVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_created_visit()
        page.save_and_bind_visit()
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.bind_visit()


class TestCreateProtocol:
    URL = 'https://nt.ris-x.com/visit/'

    def test_create_protocol(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol()
        page.save_protocol()
        page.waiting_for_notification('Данные сохранены.')
        page.sleep(5)


class TestProtocol:
    URL = 'https://nt.ris-x.com/visit/'

    def test_return_protocol_to_editable(self, driver):
        page = ProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.return_protocol_to_editable()
        page.waiting_for_notification('Документ возвращен в режим редактирования.')
        page.close_protocol()
