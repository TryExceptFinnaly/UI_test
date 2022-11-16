from pages.p_authorization import AuthorizationPage
from locators.l_patients import PatientsPageLocators as PatientsLocators
from generator.generator import generated_person


class PatientsPage(AuthorizationPage):
    def found_created_patients(self):
        patient_info = next(generated_person())
        last_name = f'{patient_info.last_name}'
        first_name = f'{patient_info.first_name}'
        middle_name = f'{patient_info.middle_name}'
        birthdate = f'{patient_info.birth_day}{patient_info.birth_month}{patient_info.birth_year}'
        self.element_is_visible(PatientsLocators.INPUT_LAST_NAME).send_keys(last_name)
        self.element_is_visible(PatientsLocators.INPUT_FIRST_NAME).send_keys(first_name)
        self.element_is_visible(PatientsLocators.INPUT_MIDDLE_NAME).send_keys(middle_name)
        self.element_is_visible(PatientsLocators.INPUT_BIRTHDAY).send_keys(birthdate)
        full_name = f'{last_name} {first_name} {middle_name}'
        birthdate = f'{patient_info.birth_day}.{patient_info.birth_month}.{patient_info.birth_year}'
        return full_name, birthdate

    def check_found_patient(self):
        self.element_is_visible(PatientsLocators.TBODY_PATIENTS)
        patient = self.elements_are_visible(PatientsLocators.PATIENT)
        return patient[3].text, patient[4].text
