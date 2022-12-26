from pages.p_main_content import MainContentPage
from locators.l_patients import PatientSearchPageLocators as PatientSearchLocators
from locators.l_patients import PatientPageLocators as PatientLocators
from data.data import SystemDirectory
from generator.generator import generated_person


class PatientsPage(MainContentPage):
    patient_info = next(generated_person())
    patient_info.full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'

    def search_created_patients(self):
        birthdate = f'{self.patient_info.birth_day}{self.patient_info.birth_month}{self.patient_info.birth_year}'
        self.element_is_visible(PatientSearchLocators.INPUT_LAST_NAME).send_keys(self.patient_info.last_name)
        self.element_is_visible(PatientSearchLocators.INPUT_FIRST_NAME).send_keys(self.patient_info.first_name)
        self.element_is_visible(PatientSearchLocators.INPUT_MIDDLE_NAME).send_keys(self.patient_info.middle_name)
        self.element_is_visible(PatientSearchLocators.INPUT_BIRTHDAY).send_keys(birthdate)
        self.element_is_visible(PatientSearchLocators.INPUT_SNILS).send_keys('112-233-445 95')
        self.element_is_visible(PatientSearchLocators.INPUT_POLIS).send_keys('PATIENT_POLIS_OMS')

    def check_found_patient(self):
        birthdate = f'{self.patient_info.birth_day}.{self.patient_info.birth_month}.{self.patient_info.birth_year}'
        sex = SystemDirectory.sex[self.patient_info.sex][0]
        return True if self.element_is_visible(
            PatientSearchLocators.get_visit_locator(name=self.patient_info.full_name, birthdate=birthdate, sex=sex,
                                                    snils='112-233-445 95', polis='PATIENT_POLIS_OMS'),
            return_false=True) else False

    def check_found_patient_in_edit_tab(self):
        self.element_is_visible(PatientSearchLocators.MODIFY_PATIENT).click()
        self.element_is_visible(PatientLocators.TAB_EDIT).click()
        last_name = f'{self.patient_info.last_name}'
        first_name = f'{self.patient_info.first_name}'
        middle_name = f'{self.patient_info.middle_name}'
        birthdate = f'{self.patient_info.birth_year}-{self.patient_info.birth_month}-{self.patient_info.birth_day}'
        sex = SystemDirectory.sex[self.patient_info.sex][0]
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_FIRST_NAME).get_attribute('value') == first_name
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_LAST_NAME).get_attribute('value') == last_name
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_MIDDLE_NAME).get_attribute('value') == middle_name
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_BIRTHDAY).get_attribute('value') == birthdate
        assert self.element_is_visible(PatientLocators.EditTab.SEX_SELECT_VALUE).text == sex
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_SNILS).get_attribute('value') == '112-233-445 95'
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_POLIS).get_attribute(
            'value') == 'PATIENT_POLIS_OMS'
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_ALTERNATE_ID).get_attribute(
            'value') == 'PATIENT_ALTER_ID'

    def save_patient(self):
        self.element_is_visible(PatientLocators.EditTab.SAVE_BUTTON).click()
        self.element_is_visible(self.Locators.LOADING_BAR)
        self.element_is_not_visible(self.Locators.LOADING_BAR)

    def save_and_continue_patient(self):
        self.element_is_visible(PatientLocators.EditTab.SAVE_AND_CONTINUE).click()
        self.element_is_visible(self.Locators.LOADING_BAR)
        self.element_is_not_visible(self.Locators.LOADING_BAR)
