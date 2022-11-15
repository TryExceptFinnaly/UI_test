import requests

from random import randint
from generator.generator import generated_person
from pages.p_authorization import AuthorizationPage
from locators.l_visit import VisitPageLocators, CreateProtocolLocators


class VisitPage(AuthorizationPage):
    locators = VisitPageLocators()

    def go_to_create_visit(self):
        button_create_visit = self.element_is_visible(self.locators.CREATE_VISIT)
        link_href = button_create_visit.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            button_create_visit.click()
        assert link_href in self.current_url()

    def go_to_created_visit(self):
        link_created_visit = self.elements_are_visible(self.locators.PATIENTS_TYPES_OF_STUDY_LIST)
        link_href = link_created_visit[0].get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link_created_visit[0].click()
        assert link_href in self.current_url()

    def fill_data_patient(self):
        patient_info = next(generated_person())
        full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthday = f'{patient_info.birth_day}{patient_info.birth_month}{patient_info.birth_year}'
        print(f'\n{patient_info}')

        self.element_is_visible(self.locators.TYPES_OF_STUDY_CONTAINER).click()
        elm_type_of_study = self.elements_are_visible(self.locators.TYPE_OF_STUDY)
        elm_type_of_study = elm_type_of_study[randint(0, len(elm_type_of_study) - 1)]
        print(elm_type_of_study.text)
        elm_type_of_study.click()

        self.element_is_visible(self.locators.SEX_CONTAINER).click()
        elm_sex = self.elements_are_visible(self.locators.SEX)
        elm_sex[randint(0, len(elm_sex) - 1)].click()

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.BIRTHDAY).send_keys(birthday)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PHONE_NUMBER).send_keys(phone_number)

        patient = f'{patient_info.last_name} {patient_info.first_name[0]}. {patient_info.middle_name[0]}.'
        return patient, patient_info.birthday

    def save_visit(self):
        self.element_is_visible(self.locators.SAVE_BUTTON, True).click()

    def select_action_variant(self, variant: int = 0):
        self.element_is_visible(self.locators.LIST_SAVE_ACTIONS, True).click()
        select_action = self.elements_are_present(self.locators.SELECT_ACTIONS)[variant]
        self.scroll_to_element(select_action)
        select_action.click()

    def waiting_for_notification(self, waiting_notification: str):
        current_notification = ''
        while current_notification != waiting_notification:
            notifications = self.elements_are_visible(self.locators.PAGE_NOTIFICATIONS)
            for n in notifications:
                current_notification = n.text
                if current_notification == waiting_notification:
                    break

    def refresh_study_page(self):
        self.element_is_visible(self.locators.REFRESH_STUDY_PAGE)
        self.element_is_clickable(self.locators.REFRESH_STUDY_PAGE).click()

    def check_result_created_visit(self):
        patient = self.elements_are_visible(self.locators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(self.locators.PATIENTS_BIRTHDAY_LIST)[0].text
        patient_birthday = patient_birthday.split()[0]
        return patient, patient_birthday


class CreateProtocolPage(AuthorizationPage):
    locators = CreateProtocolLocators()

    def create_protocol(self):
        self.elements_are_visible(self.locators.BUTTONS_CREATE_PROTOCOL)[0].click()
        self.element_is_visible(self.locators.BUTTON_CLOSE_TEMPLATE_SELECTION).click()
        protocol_frame = self.element_is_present(self.locators.PROTOCOL_FRAME)
        self.driver.switch_to.frame(protocol_frame)
        description = self.element_is_visible(self.locators.DESCRIPTION_FIELD, True)
        conclusion = self.element_is_visible(self.locators.CONCLUSION_FIELD, True)
        recommendation = self.element_is_visible(self.locators.RECOMMENDATION_FIELD, True)
        description.click()
        description.send_keys('Описание')
        conclusion.click()
        conclusion.send_keys('Заключение')
        recommendation.click()
        recommendation.send_keys('Рекомендации')

    def save_protocol(self):
        self.driver.switch_to.default_content()
        self.element_is_visible(self.locators.BUTTON_EDITABLE, True).click()
        self.element_is_visible(self.locators.BUTTON_SAVE_PROTOCOL_AND_BACK, True).click()
