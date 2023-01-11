from selenium.webdriver.common.by import By


class PlannedVisitPageLocators:
    @staticmethod
    def get_planned_visit_locator(cito: bool, name: str, sex: str, birthdate: str, study: str, room: str = '',
                                  doctor: str = '', comment: str = '', number: str = ''):
        locator = "//tr[td[2]]"
        # Required
        prefix_cito = "[td[2][strong[text()='Cito!']]]" if cito else "[td[2][not(strong[text()='Cito!'])]]"
        prefix_name = f"[td[4][span[text()='{name}']]]"
        prefix_sex = f"[td[5][text()='{sex}']]"
        prefix_birthdate = f"[td[6][text()='{birthdate}']]"
        prefix_study = f"[td[7][ul[li[text()='{study}']]]]"
        # Optional
        prefix_room = f"[td[8][span[text()='{room}']]]" if room else ''
        prefix_doctor = f"[td[9][span[text()='{doctor}']]]" if doctor else ''
        prefix_comment = f"[td[10][text()='{comment}']]" if comment else ''
        prefix_number = f"[td[4][span[span[text()='{number}']]]]" if number else ''
        locator += prefix_cito + prefix_name + prefix_sex + prefix_birthdate + prefix_study + prefix_room + prefix_doctor + prefix_comment + prefix_number
        # print(locator)
        return By.XPATH, locator

    BUTTON_REGISTER_PLANNED_VISIT = (By.CSS_SELECTOR,
                                     'table.table.table-bordered.table-condensed.planned-list-table>tbody>tr:nth-child(1)>td>a:nth-child(2)')


class CreatePlannedVisitPageLocators:
    POLIS_OMS = (By.CSS_SELECTOR, "input#patient_polis_number")
    SNILS = (By.CSS_SELECTOR, "label.control-label[for='snils']+input.form-control")
