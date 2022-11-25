from pages.p_authorization import AuthorizationPage
from locators.l_patients import PatientSearchPageLocators as PatientSearchLocators
from locators.l_patients import PatientPageLocators as PatientLocators
from data.data import SystemDirectory
from generator.generator import generated_person


class PatientsPage(AuthorizationPage):
    patient_info = next(generated_person())

    def found_created_patients(self):
        last_name = f'{self.patient_info.last_name}'
        first_name = f'{self.patient_info.first_name}'
        middle_name = f'{self.patient_info.middle_name}'
        birthdate = f'{self.patient_info.birth_day}{self.patient_info.birth_month}{self.patient_info.birth_year}'
        self.element_is_visible(PatientSearchLocators.INPUT_LAST_NAME).send_keys(last_name)
        self.element_is_visible(PatientSearchLocators.INPUT_FIRST_NAME).send_keys(first_name)
        self.element_is_visible(PatientSearchLocators.INPUT_MIDDLE_NAME).send_keys(middle_name)
        self.element_is_visible(PatientSearchLocators.INPUT_BIRTHDAY).send_keys(birthdate)
        self.element_is_visible(PatientSearchLocators.INPUT_SNILS).send_keys('112-233-445 95')
        self.element_is_visible(PatientSearchLocators.INPUT_POLIS).send_keys('PATIENT_POLIS_OMS')
        full_name = f'{last_name} {first_name} {middle_name}'
        birthdate = f'{self.patient_info.birth_day}.{self.patient_info.birth_month}.{self.patient_info.birth_year}'
        return full_name, birthdate

    def check_found_patient(self):
        self.element_is_visible(PatientSearchLocators.TBODY_PATIENTS)
        patient = self.elements_are_visible(PatientSearchLocators.PATIENT)
        return patient[3].text, patient[4].text

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
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_POLIS).get_attribute('value') == 'PATIENT_POLIS_OMS'
        assert self.element_is_visible(PatientLocators.EditTab.INPUT_ALTERNATE_ID).get_attribute('value') == 'PATIENT_ALTER_ID'

    def save_patient(self):
        self.element_is_visible(PatientLocators.EditTab.SAVE_BUTTON).click()

    def save_and_continue_patient(self):
        self.element_is_visible(PatientLocators.EditTab.SAVE_AND_CONTINUE).click()
