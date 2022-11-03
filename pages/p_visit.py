from random import randint

import requests

from generator.generator import generated_person
from pages.p_authorization import AuthorizationPage
from locators.l_visit import VisitPageLocators as Locators


class VisitPage(AuthorizationPage):

    def go_to_create_visit(self):
        button_create_visit = self.element_is_visible(Locators.CREATE_VISIT)
        link_href = button_create_visit.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            button_create_visit.click()
        assert link_href in self.current_url()

    def fill_data_patient(self):
        patient_info = next(generated_person())
        full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthday = patient_info.birthday
        print(f'\n{patient_info}')

        self.element_is_visible(Locators.TYPES_OF_STUDY_CONTAINER).click()
        elm_type_of_study = self.elements_are_visible(Locators.TYPE_OF_STUDY)
        elm_type_of_study[randint(0, len(elm_type_of_study) - 1)].click()

        self.element_is_visible(Locators.SEX_CONTAINER).click()
        elm_sex = self.elements_are_visible(Locators.SEX)
        elm_sex[randint(0, len(elm_sex) - 1)].click()

        self.element_is_visible(Locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(Locators.BIRTHDAY).send_keys(birthday)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PHONE_NUMBER).send_keys(phone_number)

        patient = f'{patient_info.last_name} {patient_info.first_name[0]}. {patient_info.middle_name[0]}.'
        return patient, patient_info.birthday

    def create_visit(self):
        self.go_to_element(self.element_is_present(Locators.SAVE_BUTTON))
        self.element_is_visible(Locators.SAVE_BUTTON).click()

    def check_result_created_visit(self):
        self.element_is_clickable(Locators.REFRESH_STUDY_PAGE).click()
        patient = self.elements_are_visible(Locators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(Locators.PATIENTS_BIRTHDAY_LIST)[0].text
        patient_birthday = patient_birthday.split()[0].replace('.', '-')
        # result = [i.text for i in result]
        return patient, patient_birthday
