from generator.generator import generated_person
from pages.authorization_page import AuthorizationPage
from locators.create_visit_locator import AuthorizationPageLocators as Locators


class CreateVisitPage(AuthorizationPage):

    def submit_and_fill_fields(self):
        patient_info = next(generated_person())
        full_name = patient_info.full_name
        email = patient_info.email
        phone_number = patient_info.phone_number
        self.element_is_visible(Locators.CREATE_VISIT).click()
        self.element_is_visible(Locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PHONE_NUMBER).send_keys(phone_number)

    def check_data_page(self):
        pass
