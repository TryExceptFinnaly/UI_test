import allure

from pages.p_visit import VisitPage, CreateVisitPage, BindVisitPage, CreateProtocolPage, ProtocolPage


@allure.feature('Visit Page')
class TestVisitPage:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Refresh page')
    def test_refresh_page(self, driver):
        page = VisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.refresh_study_page()


@allure.feature('Create Visit')
class TestCreateVisit:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Create visit')
    def test_create_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('close')
        page.waiting_for_notification('Данные сохранены.')
        data = page.check_result_created_visit()
        assert entered_data == data
        print(f'Entered data: {entered_data}')
        print(f'Data: {data}')


@allure.feature('Protocol')
class TestProtocol:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Create protocol from visit page and delete')
    def test_work_protocol_visit_page(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol('visit_page')
        page.save_protocol()
        page.open_visit('available')
        page.delete_protocol()

    @allure.title('Create protocol from reg form and delete')
    def test_work_protocol_reg_form(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol('reg_form')
        page.save_protocol()
        page.open_visit('available')
        page.delete_protocol()

    @allure.title('Create protocol from tab doc')
    def test_work_protocol_tab_doc(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol('tab_doc')
        page.save_protocol()

    @allure.title('Return protocol to edit mode')
    def test_return_protocol_to_editable(self, driver):
        page = ProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.return_protocol_to_editable()
        page.close_protocol()

    @allure.title('Delete protocol')
    def test_delete_protocol(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_visit('available')
        page.delete_protocol()


@allure.feature('Visit')
class TestVisit:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Bind visit')
    def test_bind_visit(self, driver):
        page = BindVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_visit('ignore')
        page.save_visit('bind')
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.bind_visit()

    @allure.title('Delete visit')
    def test_delete_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_visit('ignore')
        page.delete_visit()
