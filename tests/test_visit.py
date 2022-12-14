import allure

from pages.p_visit import VisitPage, CreateVisitPage, ImageVisitPage, CreateProtocolPage, ProtocolPage
from hl7.hl7 import send_hl7_message


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

    @allure.title('Create and continue visit')
    def test_create_and_continue_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('continue')
        page.waiting_for_notification('Данные сохранены.')
        assert (self.URL in page.current_url()) and (self.URL != page.current_url()), 'Incorrect current URL'

    @allure.title('Create and close visit')
    def test_create_and_close_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('close')
        page.waiting_for_notification('Данные сохранены.')
        data = page.check_result_created_visit()
        assert entered_data == data, 'The data entered does not match the data received'
        assert self.URL == page.current_url(), 'Incorrect current URL'

    @allure.title('Create and create new visit')
    def test_create_and_create_new_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('create')
        page.waiting_for_notification('Данные сохранены.')
        assert f'{self.URL}create/' in page.current_url(), 'Incorrect current URL'

    @allure.title('Create and bind visit')
    def test_create_and_bind_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('bind')
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.bind_visit()
        data = page.check_result_created_visit()
        assert entered_data == data, 'The data entered does not match the data received'
        assert self.URL == page.current_url(), 'Incorrect current URL'

    @allure.title('Create and bind and create new visit')
    def test_create_and_bind_and_create_new_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_visit()
        entered_data = page.fill_all_fields()
        page.save_visit('bind_and_create')
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.bind_visit()
        assert f'{self.URL}create/' in page.current_url(), 'Incorrect current URL'

    # def test_document(self, driver):
    #     page = CreateVisitPage(driver, self.URL)
    #     page.open()
    #     page.authorization()
    #     page.go_to_create_visit()
    #     page.fill_document_and_save()


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
        count, locator = page.list_visits_on_page('present')
        page.open_visit(locator)
        page.delete_protocol()

    @allure.title('Create protocol from reg form and delete')
    def test_work_protocol_reg_form(self, driver):
        page = CreateProtocolPage(driver, self.URL)
        page.open()
        page.authorization()
        page.create_protocol('reg_form')
        page.save_protocol()
        count, locator = page.list_visits_on_page('present')
        page.open_visit(locator)
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
        count, locator = page.list_visits_on_page('present')
        page.open_visit(locator)
        page.delete_protocol()


@allure.feature('Image Visit')
class TestImageVisit:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Delete image from visit')
    def test_delete_image_from_visit(self, driver):
        page = ImageVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        before_count = page.open_image_from_visit()
        answer_count = page.delete_image_from_visit()
        assert before_count == answer_count, 'Before and answer counts do not differ'


@allure.feature('Visit')
class TestVisit:
    URL = 'https://nt.ris-x.com/visit/'

    @allure.title('Bind visit')
    def test_bind_visit(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        count, locator = page.list_visits_on_page()
        page.open_visit(locator)
        page.save_visit('bind')
        page.waiting_for_notification('Данные сохранены.')
        if not page.waiting_for_notification('Сопоставление успешно выполнено.', return_false=True):
            page.bind_visit()

    @allure.title('Bind visit from HL7 message(SC Accession Number)')
    def test_bind_visit_from_hl7_message(self, driver):
        page = VisitPage(driver, self.URL)
        page.open()
        page.authorization()
        count, locator = page.list_visits_on_page(image='missing', wlm='present')
        for i in range(count):
            page.refresh_study_page()
            acc_number = page.get_visit_id(locator)
            result = send_hl7_message(f'sc_{acc_number}')
            print(result)
            page.sleep(5)

    @allure.title('Delete visits')
    def test_delete_visits(self, driver):
        page = CreateVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        count, locator = page.list_visits_on_page()
        for i in range(count):
            page.open_visit(locator)
            page.delete_visit()
            page.refresh_study_page()
