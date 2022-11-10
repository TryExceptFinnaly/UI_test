from pages.p_authorization import AuthorizationPage
from locators.l_patients import PatientsPageLocators
from generator.generator import generated_person


class PatientsPage(AuthorizationPage):
    locators = PatientsPageLocators()

    def check_created_patients(self):
        patient_info = next(generated_person())
        last_name = f'{patient_info.last_name}'
        first_name = f'{patient_info.first_name}'
        middle_name = f'{patient_info.middle_name}'
        birthday = patient_info.birthday.replace('.', '')
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.INPUT_MIDDLE_NAME).send_keys(middle_name)
        self.element_is_visible(self.locators.INPUT_BIRTHDAY).send_keys(birthday)
