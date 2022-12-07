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
        entered_name, entered_birthdate = page.found_created_patients()
        name, birthdate = page.check_found_patient()
        assert (entered_name, entered_birthdate) == (name, birthdate)
        page.check_found_patient_in_edit_tab()
        page.save_and_continue_patient()
        page.waiting_for_notification('Данные сохранены.')
        page.save_patient()
        page.waiting_for_notification('Данные сохранены.')
