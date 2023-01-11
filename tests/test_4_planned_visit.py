import allure

from pages.p_planned_visit import PlannedVisitPage, CreatePlannedVisitPage
from hl7.hl7 import send_hl7_message


@allure.feature('Planned Visits')
class TestPlannedVisit:
    URL = 'https://nt.ris-x.com/planned/'

    @allure.title('Create planned visit(HL7 msg)')
    def test_create_planned_visit_in_hl7_message(self, driver):
        page = PlannedVisitPage(driver, self.URL)
        result = send_hl7_message('nw', patient_info=page.patient_info, count=2)
        print(result)
        page.open()
        page.authorization()
        assert page.get_planned_visit(), 'Planned visit not found'

    @allure.title('Check data planned visit')
    def test_check_data_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_create_planned_visit()
        page.check_all_fields()

    @allure.title('Register planned visit')
    def test_register_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_create_planned_visit()
        page.register_planned_visit()

    @allure.title('Delete planned visit')
    def test_delete_planned_visit(self, driver):
        page = CreatePlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.open_create_planned_visit()
        page.delete_planned_visit()
