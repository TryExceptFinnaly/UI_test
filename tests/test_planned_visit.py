import subprocess

from pages.p_planned_visit import PlannedVisitPage
from time import sleep


class TestPlannedVisitPage:
    URL = 'https://nt.ris-x.com/planned/'

    @staticmethod
    def send_hl7_message():
        path_to_hl7 = r'C:/Users/LINS/PycharmProjects/UI_test/hl7/'
        cmd = f'{path_to_hl7}HL7_cmd.exe -i nt.ris-x.com -fp {path_to_hl7}test_nw.hl7 -r 1'
        returned_output = subprocess.check_output(cmd)
        print(returned_output.decode('cp1251'))

    def test_create_planned_visit_in_hl7_message(self, driver):
        self.send_hl7_message()
        page = PlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.check_list_planned_visits()
        sleep(5)

    def test_register_a_planned_visit(self, driver):
        page = PlannedVisitPage(driver, self.URL)
        page.open()
        page.authorization()
        page.register_a_planned_visit()
        sleep(5)
