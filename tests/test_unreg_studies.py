import allure

from pages.p_unreg_studies import UnregStudiesPage
from hl7.hl7 import send_hl7_message


@allure.feature('Unreg Studies')
class TestUnregStudies:
    URL = 'https://nt.ris-x.com/unreg/'

    @allure.title('Create unreg studies from HL7 message')
    def test_create_unreg_study_from_hl7_message(self, driver):
        send_hl7_message('sc', count=3)  # True
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        assert page.get_unreg_study(), 'Unregistered study not found'
