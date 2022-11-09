import subprocess

from pages.p_unreg_studies import UnregStudiesPage
from time import sleep

class TestUnregStudiesPage:
    URL = 'https://nt.ris-x.com/unreg/'

    @staticmethod
    def send_hl7_message():
        path_to_hl7 = r'C:/Users/LINS/PycharmProjects/UI_test/hl7/'
        cmd = f'{path_to_hl7}HL7_cmd.exe -i nt.ris-x.com -fp {path_to_hl7}test_sc.hl7 -r 1'
        returned_output = subprocess.check_output(cmd)
        print(returned_output.decode('cp1251'))

    def test_create_unreg_study_in_hl7_message(self, driver):
        self.send_hl7_message()
        page = UnregStudiesPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_list_unreg_studies()
        sleep(5)
