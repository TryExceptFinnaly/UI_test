import requests

from generator.generator import generated_person
from pages.p_authorization import AuthorizationPage
from locators.l_visit import VisitPageLocators as VisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from locators.l_visit import CreateProtocolPageLocators as CreateProtocolLocators


class VisitPage(AuthorizationPage):

    def go_to_create_visit(self):
        button_create_visit = self.element_is_visible(VisitLocators.CREATE_VISIT)
        link_href = button_create_visit.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            button_create_visit.click()
        assert link_href in self.current_url()

    def go_to_created_visit(self):
        link_created_visit = self.elements_are_visible(VisitLocators.PATIENTS_TYPES_OF_STUDY_LIST)
        link_href = link_created_visit[0].get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link_created_visit[0].click()
        assert link_href in self.current_url()

    def waiting_for_notification(self, waiting_notification: str):
        current_notification = ''
        while current_notification != waiting_notification:
            notifications = self.elements_are_visible(VisitLocators.PAGE_NOTIFICATIONS)
            for n in notifications:
                current_notification = n.text
                if current_notification == waiting_notification:
                    break

    def refresh_study_page(self):
        self.element_is_visible(VisitLocators.REFRESH_STUDY_PAGE)
        self.element_is_clickable(VisitLocators.REFRESH_STUDY_PAGE).click()

    def check_result_created_visit(self):
        patient = self.elements_are_visible(VisitLocators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(VisitLocators.PATIENTS_BIRTHDAY_LIST)[0].text
        patient_birthday = patient_birthday.split()[0]
        return patient, patient_birthday


class CreateVisitPage(VisitPage):

    def fill_data_patient(self):
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        patient_info = next(generated_person())
        full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthdate = f'{patient_info.birth_day}{patient_info.birth_month}{patient_info.birth_year}'
        print(f'\n{patient_info}')

        self.element_is_visible(CreateVisitLocators.EXTERNAL_ID).send_keys('PATIENT_ID')
        self.element_is_visible(CreateVisitLocators.POLIS_OMS).send_keys('PATIENT_POLIS_OMS')
        self.element_is_clickable(CreateVisitLocators.SNILS)
        snils = self.element_is_visible(CreateVisitLocators.SNILS)
        self.click_and_send_keys(snils, '14858733210')
        self.element_is_visible(CreateVisitLocators.FULL_NAME).send_keys(full_name)
        self.element_is_clickable(CreateVisitLocators.BIRTHDAY)
        birthday = self.element_is_visible(CreateVisitLocators.BIRTHDAY)
        self.click_and_send_keys(birthday, birthdate)
        self.element_is_visible(CreateVisitLocators.SEX_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.SEX, random_element=True).click()
        self.element_is_visible(CreateVisitLocators.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(CreateVisitLocators.EMAIL).send_keys(email)
        self.element_is_visible(CreateVisitLocators.ALLERGY_TYPE_CONTAINER).click()
        # allergy_type = self.elements_are_visible(CreateVisitLocators.ALLERGY_TYPE, random_element=True)
        # self.scroll_to_element(allergy_type)
        # allergy_type.click()
        self.element_is_visible(CreateVisitLocators.YEAR_DOSE)

        self.element_is_visible(CreateVisitLocators.TREATMENT_CASE_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.TREATMENT_CASE, random_element=True).click()
        self.element_is_visible(CreateVisitLocators.PATIENT_CLASS_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.PATIENT_CLASS, random_element=True).click()
        self.element_is_visible(CreateVisitLocators.OUTPATIENT_CARD_NUMBER).send_keys('OUTPATIENT_CARD_NUMBER')
        self.element_is_visible(CreateVisitLocators.CASE_HISTORY_NUMBER).send_keys('CASE_HISTORY_NUMBER')
        self.element_is_visible(CreateVisitLocators.REF_DEPARTMENT).send_keys('REF_DEPARTMENT')
        self.element_is_visible(CreateVisitLocators.REF_DOCTOR).send_keys('REF_DOCTOR')
        self.element_is_visible(CreateVisitLocators.SOURCE_FINANCING_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.SOURCE_FINANCING, random_element=True).click()
        self.element_is_visible(CreateVisitLocators.PURPOSE).send_keys('PURPOSE')
        self.element_is_visible(CreateVisitLocators.COMMENT).send_keys('COMMENT')

        self.element_is_visible(CreateVisitLocators.DOCTOR_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.ASSISTANT_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.TYPES_OF_STUDY_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.TYPE_OF_STUDY, random_element=True).click()
        self.element_is_visible(CreateVisitLocators.DEVICE_CONTAINER)
        self.element_is_visible(CreateVisitLocators.CONTRAST_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.CONTRAST_VOLUME).click()
        self.element_is_visible(CreateVisitLocators.DOSE_RG).click()
        self.element_is_visible(CreateVisitLocators.DOSE)
        self.element_is_visible(CreateVisitLocators.IS_CITO_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.IS_CITO, random_element=True).click()

        patient = f'{patient_info.last_name} {patient_info.first_name[0]}. {patient_info.middle_name[0]}.'
        birthdate = f'{patient_info.birth_day}.{patient_info.birth_month}.{patient_info.birth_year}'
        return patient, birthdate

    def select_action_variant(self, variant: int = 0):
        self.element_is_visible(CreateVisitLocators.LIST_SAVE_ACTIONS, True).click()
        select_action = self.elements_are_present(CreateVisitLocators.SELECT_ACTIONS)[variant]
        self.scroll_to_element(select_action)
        select_action.click()

    def save_visit(self):
        self.element_is_visible(CreateVisitLocators.SAVE_BUTTON, True).click()

    def delete_visit(self):
        self.element_is_visible(CreateVisitLocators.DELETE_BUTTON).click()
        self.element_is_visible(CreateVisitLocators.REASON_FOR_DELETE).send_keys('Reason for delete')
        self.element_is_visible(CreateVisitLocators.MODAL_ACTION_DELETE).click()


class CreateProtocolPage(VisitPage):
    def create_protocol(self):
        self.elements_are_visible(CreateProtocolLocators.BUTTONS_CREATE_PROTOCOL)[0].click()
        self.element_is_visible(CreateProtocolLocators.BUTTON_CLOSE_TEMPLATE_SELECTION).click()
        protocol_frame = self.element_is_present(CreateProtocolLocators.PROTOCOL_FRAME)
        self.driver.switch_to.frame(protocol_frame)
        description = self.element_is_visible(CreateProtocolLocators.DESCRIPTION_FIELD, True)
        conclusion = self.element_is_visible(CreateProtocolLocators.CONCLUSION_FIELD, True)
        recommendation = self.element_is_visible(CreateProtocolLocators.RECOMMENDATION_FIELD, True)
        description.click()
        description.send_keys('Описание')
        conclusion.click()
        conclusion.send_keys('Заключение')
        recommendation.click()
        recommendation.send_keys('Рекомендации')

    def save_protocol(self):
        self.driver.switch_to.default_content()
        self.element_is_visible(CreateProtocolLocators.BUTTON_EDITABLE, True).click()
        self.element_is_visible(CreateProtocolLocators.BUTTON_SAVE_PROTOCOL_AND_BACK, True).click()
