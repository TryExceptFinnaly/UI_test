import allure

from pages.p_patients import PatientsPage


@allure.feature('Patients')
class TestPatients:
    URL = 'https://nt.ris-x.com/patients/'

    @allure.title('Found patient, tab edit - save')
    def test_created_patient(self, driver):
        page = PatientsPage(driver, self.URL)
        page.open()
        page.authorization()
        page.search_created_patients()
        assert page.check_found_patient(), 'The data entered does not match the data received'
        page.check_found_patient_in_edit_tab()
        page.save_and_continue_patient()
        page.waiting_for_notification('Данные сохранены.')
        page.sleep(3)
        page.save_patient()
        page.waiting_for_notification('Данные сохранены.')
        assert self.URL == page.current_url(), 'Incorrect current URL'
