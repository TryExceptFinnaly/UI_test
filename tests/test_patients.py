from pages.p_patients import PatientsPage
from time import sleep


class TestPatientsPage:
    URL = 'https://nt.ris-x.com/patients/'

    def test_created_patient(self, driver):
        page = PatientsPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_created_patients()
        sleep(5)
