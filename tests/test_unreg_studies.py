import allure

from pages.p_unreg_studies import UnregStudiesPage
from hl7.hl7 import send_hl7_message


@allure.feature('Unreg Studies')
class TestUnregStudies:
    URL = 'https://nt.ris-x.com/unreg/'

    @allure.title('Create unreg studies from HL7 message')
    def test_create_unreg_study_from_hl7_message(self, driver):
        send_hl7_message('sc', count=5)  # True
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        assert page.get_unreg_study(), 'Unregistered study not found'

    @allure.title('Delete unreg study')
    def test_delete_unreg_study(self, driver):
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        unreg_study = page.get_unreg_study()
        before_count = len(unreg_study)
        page.delete_unreg_study(unreg_study)
        page.refresh_page()
        page.refresh_page()
        unreg_study = page.get_unreg_study()
        after_count = len(unreg_study)
        assert before_count != after_count, 'Counts before and after do not differ'

