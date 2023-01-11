import allure

from pages.p_unreg_studies import UnregStudiesPage
from hl7.hl7 import send_hl7_message


@allure.feature('Unreg Studies')
class TestUnregStudies:
    URL = 'https://nt.ris-x.com/unreg/'
    COUNT = 3

    @allure.title('Create unreg studies from HL7 message')
    def test_create_unreg_study_from_hl7_message(self, driver):
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        # Generate new patient!!!
        page.generate_new_patient(777)
        before_unreg_studies = page.get_unreg_studies()
        send_hl7_message('sc', patient_info=page.patient_info, count=self.COUNT)  # True
        page.sleep(5)
        page.refresh_page()
        after_unreg_studies = page.get_unreg_studies()
        assert after_unreg_studies, 'Unregistered study not found'
        count_unreg_studies = len(after_unreg_studies) if not before_unreg_studies else (
                len(after_unreg_studies) - len(before_unreg_studies))
        assert count_unreg_studies == self.COUNT, 'The number of sent and received messages differs'

    @allure.title('Delete unreg study')
    def test_delete_unreg_study(self, driver):
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        unreg_study = page.get_unreg_studies()
        before_count = len(unreg_study)
        page.delete_unreg_study(unreg_study)
        page.refresh_page()
        page.refresh_page()
        unreg_study = page.get_unreg_studies()
        after_count = len(unreg_study)
        assert before_count != after_count, 'Counts before and after do not differ'
