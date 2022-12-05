import allure

from pages.p_planned_visit import PlannedVisitPage, CreatePlannedVisitPage
from hl7.hl7 import send_hl7_message


@allure.feature('Planned Visits')
class TestPlannedVisit:
    URL = 'https://nt.ris-x.com/planned/'

    @allure.title('Create planned visit(HL7 msg)')
    def test_create_planned_visit_in_hl7_message(self, driver):
        send_hl7_message('nw', count=2)
        page = PlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_list_planned_visits()
        page.sleep(5)

    @allure.title('Check data planned visit')
    def test_check_data_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_planned_visit()
        page.check_base_planned_visit()
        page.check_params_planned_visit()
        page.check_additional_planned_visit()
        page.check_passport_registration_planned_visit()

    @allure.title('Register planned visit')
    def test_register_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_planned_visit()
        page.register_planned_visit()
        page.sleep(5)

    @allure.title('Delete planned visit')
    def test_delete_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.go_to_create_planned_visit()
        page.delete_planned_visit()
        page.sleep(5)
