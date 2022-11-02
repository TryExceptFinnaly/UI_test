from random import randint

from generator.generator import generated_person
from pages.authorization_page import AuthorizationPage
from locators.elements_locators_page import CreateVisitPageLocators as Locators


class CreateVisitPage(AuthorizationPage):

    def submit_and_fill_fields(self):
        patient_info = next(generated_person())
        full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthday = patient_info.birthday

        print(patient_info)

        self.element_is_visible(Locators.CREATE_VISIT).click()

        self.element_is_visible(Locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)

        self.element_is_visible(Locators.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(Locators.BIRTHDAY).send_keys(birthday)

        self.element_is_clickable(Locators.SEX_CONTAINER).click()
        elm_sex = self.elements_are_visible(Locators.SEX)
        elm_sex[randint(0, len(elm_sex) - 1)].click()

        self.element_is_clickable(Locators.TYPES_OF_STUDY_CONTAINER).click()
        elm_types_of_study = self.elements_are_visible(Locators.TYPES_OF_STUDY)
        elm_types_of_study[randint(0, len(elm_types_of_study) - 1)].click()

        self.go_to_element(self.element_is_present(Locators.SAVE_BUTTON))
        self.element_is_clickable(Locators.SAVE_BUTTON).click()
        patient = f'{patient_info.last_name} {patient_info.first_name[0]}. {patient_info.middle_name[0]}.'
        return patient, patient_info.birthday

    def check_data_page(self):
        self.element_is_clickable(Locators.REFRESH_STUDY_PAGE).click()
        patient = self.elements_are_visible(Locators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(Locators.PATIENTS_BIRTHDAY_LIST)[0].text
        patient_birthday = patient_birthday.split()[0].replace('.', '-')
        # result = [i.text for i in result]
        return patient, patient_birthday
