from random import randint

from generator.generator import generated_person
from pages.authorization_page import AuthorizationPage
from locators.elements_locators_page import CreateVisitPageLocators as Locators


class CreateVisitPage(AuthorizationPage):

    def submit_and_fill_fields(self):
        patient_info = next(generated_person())
        full_name = patient_info.full_name
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthday = patient_info.birthday

        print(patient_info)

        self.element_is_visible(Locators.CREATE_VISIT).click()
        self.element_is_visible(Locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)

        self.element_is_visible(Locators.PHONE_NUMBER).send_keys(phone_number)

        elm_birthday = self.element_is_visible(Locators.BIRTHDAY)
        elm_birthday.click()
        elm_birthday.send_keys(birthday)

        self.element_is_visible(Locators.GENDER_CONTAINER).click()
        elm_genders = self.elements_are_visible(Locators.GENDER)
        elm_genders[randint(0, len(elm_genders) - 1)].click()

        self.element_is_visible(Locators.TYPES_OF_STUDY_CONTAINER).click()
        elm_types_of_study = self.elements_are_visible(Locators.TYPES_OF_STUDY)
        elm_types_of_study[randint(0, len(elm_types_of_study) - 1)].click()

        elm_save_button = self.element_is_visible(Locators.SAVE_BUTTON)
        self.go_to_element(elm_save_button)
        elm_save_button.click()
        # self.element_is_visible(Locators.SAVE_BUTTON).click()

    def check_data_page(self):
        return self.current_url()
