from pages.p_patients import PatientsPage


class TestPatientsPage:
    URL = 'https://nt.ris-x.com/patients/'

    def test_created_patient(self, driver):
        page = PatientsPage(driver, self.URL)
        page.open()
        page.authorization()
        entered_name, entered_birthdate = page.found_created_patients()
        name, birthdate = page.check_found_patient()
        assert (entered_name, entered_birthdate) == (name, birthdate)
        page.sleep(5)
