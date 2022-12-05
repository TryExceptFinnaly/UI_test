from pages.p_unreg_studies import UnregStudiesPage
from hl7.hl7 import send_hl7_message


class TestUnregStudies:
    URL = 'https://nt.ris-x.com/unreg/'

    def test_create_unreg_study_in_hl7_message(self, driver):
        send_hl7_message('sc', count=2)  # True
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_list_unreg_studies()
        page.sleep(5)
