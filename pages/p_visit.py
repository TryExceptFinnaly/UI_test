from data.data import SystemDirectory
from generator.generator import generated_person
from pages.p_authorization import AuthorizationPage
from locators.l_visit import VisitPageLocators as VisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from locators.l_visit import ComparisonVisitPageLocators as ComparisonVisitLocators
from locators.l_visit import CreateProtocolPageLocators as CreateProtocolLocators


class VisitPage(AuthorizationPage):

    def go_to_create_visit(self):
        button_create_visit = self.element_is_visible(VisitLocators.CREATE_VISIT)
        link_href = button_create_visit.get_attribute('href')
        request = self.get_request(link_href)
        if request.status_code == 200:
            button_create_visit.click()
        assert link_href in self.current_url()

    def go_to_created_visit(self):
        link_created_visit = self.elements_are_visible(VisitLocators.PATIENTS_TYPES_OF_STUDY_LIST)
        link_href = link_created_visit[0].get_attribute('href')
        request = self.get_request(link_href)
        if request.status_code == 200:
            link_created_visit[0].click()
        assert link_href in self.current_url()

    def refresh_study_page(self):
        self.element_is_visible(VisitLocators.REFRESH_STUDY_PAGE)
        self.element_is_clickable(VisitLocators.REFRESH_STUDY_PAGE).click()

    def check_result_created_visit(self):
        patient = self.elements_are_visible(VisitLocators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(VisitLocators.PATIENTS_BIRTHDAY_LIST)[0].text
        patient_birthday = patient_birthday.split()[0]
        return patient, patient_birthday


class CreateVisitPage(VisitPage):
    patient_info = next(generated_person())

    def fill_base_fields_patient(self):
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_visible(CreateVisitLocators.TAB_BASE).click()

        full_name = f'{self.patient_info.last_name} {self.patient_info.first_name} {self.patient_info.middle_name}'
        email = self.patient_info.email
        phone_number = self.patient_info.phone_number
        birthdate = f'{self.patient_info.birth_day}{self.patient_info.birth_month}{self.patient_info.birth_year}'
        sex = SystemDirectory.sex[self.patient_info.sex][1]
        allergy_type = SystemDirectory.allergy_type[self.patient_info.allergy_type][1]
        treatment_case = SystemDirectory.treatment_case[self.patient_info.treatment_case][1]
        patient_class = SystemDirectory.patient_class[self.patient_info.patient_class][1]
        is_cito = SystemDirectory.is_cito[self.patient_info.is_cito][1]
        print(f'\n{self.patient_info}')

        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_visible(CreateVisitLocators.BaseTab.EXTERNAL_ID).send_keys('PATIENT_ID')
        self.element_is_visible(CreateVisitLocators.BaseTab.POLIS_OMS).send_keys('PATIENT_POLIS_OMS')
        # self.element_is_clickable(CreateVisitLocators.BaseTab.SNILS)
        self.element_is_visible(CreateVisitLocators.BaseTab.SNILS).send_keys('000-000-000 00')
        # self.click_and_send_keys(snils, '000-000-000 00')
        self.element_is_visible(CreateVisitLocators.BaseTab.FULL_NAME).send_keys(full_name)
        self.element_is_clickable(CreateVisitLocators.BaseTab.BIRTHDAY)
        birthday = self.element_is_visible(CreateVisitLocators.BaseTab.BIRTHDAY)
        self.click_and_send_keys(birthday, birthdate)
        self.element_is_visible(CreateVisitLocators.BaseTab.SEX_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.SEX, element=sex).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(CreateVisitLocators.BaseTab.EMAIL).send_keys(email)
        self.element_is_visible(CreateVisitLocators.BaseTab.ALLERGY_TYPE_CONTAINER).click()
        # allergy_type = self.elements_are_visible(CreateVisitLocators.BaseTab.ALLERGY_TYPE, element=allergy_type)
        # self.scroll_to_element(allergy_type)
        # allergy_type.click()
        self.element_is_visible(CreateVisitLocators.BaseTab.YEAR_DOSE)

        self.element_is_visible(CreateVisitLocators.BaseTab.TREATMENT_CASE_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.TREATMENT_CASE, element=treatment_case).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.PATIENT_CLASS_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.PATIENT_CLASS, element=patient_class).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.OUTPATIENT_CARD_NUMBER).send_keys('OUTPATIENT_CARD_NUMBER')
        self.element_is_visible(CreateVisitLocators.BaseTab.CASE_HISTORY_NUMBER).send_keys('CASE_HISTORY_NUMBER')
        self.element_is_visible(CreateVisitLocators.BaseTab.REF_DEPARTMENT).send_keys('REF_DEPARTMENT')
        self.element_is_visible(CreateVisitLocators.BaseTab.REF_DOCTOR).send_keys('REF_DOCTOR')
        self.element_is_visible(CreateVisitLocators.BaseTab.SOURCE_FINANCING_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.SOURCE_FINANCING, element=-1).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.PURPOSE).send_keys('PURPOSE')

        self.element_is_visible(CreateVisitLocators.BaseTab.DIAGNOSES_MKB_CONTAINER).click()
        self.select_node_in_jstree(CreateVisitLocators.BaseTab.DIAGNOSES_MKB_NODES, -1)
        self.element_is_visible(CreateVisitLocators.BaseTab.DIAGNOSES_MKB_CONTAINER).click()

        self.element_is_visible(CreateVisitLocators.BaseTab.COMMENT).send_keys('COMMENT')

        self.element_is_visible(CreateVisitLocators.BaseTab.DOCTOR_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.ASSISTANT_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.TYPES_OF_STUDY_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.TYPE_OF_STUDY, element=-1).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.DEVICE_CONTAINER)
        self.element_is_visible(CreateVisitLocators.BaseTab.CONTRAST_CONTAINER).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.CONTRAST_VOLUME).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.DOSE_RG).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.DOSE)
        self.element_is_visible(CreateVisitLocators.BaseTab.IS_CITO_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.IS_CITO, element=is_cito).click()

        patient = f'{self.patient_info.last_name} {self.patient_info.first_name[0]}. {self.patient_info.middle_name[0]}.'
        birthdate = f'{self.patient_info.birth_day}.{self.patient_info.birth_month}.{self.patient_info.birth_year}'
        return patient, birthdate

    def fill_params_fields_patient(self):
        self.element_is_visible(CreateVisitLocators.TAB_PARAMS).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_COMPANY_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.ParamsTab.INSURANCE_COMPANY, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_CONTRACT).send_keys('_INSURANCE_CONTRACT')
        self.element_is_visible(CreateVisitLocators.ParamsTab.POLIS_NUMBER).send_keys('_PATIENT_POLIS')
        self.element_is_visible(CreateVisitLocators.ParamsTab.MEDICAL_DIAGNOSIS).send_keys('MEDICAL_DIAGNOSIS')
        self.element_is_visible(CreateVisitLocators.ParamsTab.ALTERNATE_ID).send_keys('PATIENT_ALTER_ID')
        self.element_is_visible(CreateVisitLocators.ParamsTab.HEIGHT).send_keys(180)
        self.element_is_visible(CreateVisitLocators.ParamsTab.WEIGHT).send_keys(80)
        self.element_is_visible(CreateVisitLocators.ParamsTab.FILM_COUNT).send_keys(3)
        self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_SIGN_CONTAINER).click()
        if self.element_is_not_visible(CreateVisitLocators.ParamsTab.FLU_SIGN_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.FLU_SIGN, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE_CONTAINER).click()
        if self.element_is_not_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.REF_ID).send_keys('REF_ID')
        self.element_is_visible(CreateVisitLocators.ParamsTab.REF_DATE).send_keys(12112022)
        self.element_is_visible(CreateVisitLocators.ParamsTab.DIRECTION_TYPE_CONTAINER).click()
        # self.elements_are_visible(CreateVisitLocators.ParamsTab.DIRECTION_TYPE, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.BENEFIT_CONTAINER).click()
        # self.elements_are_visible(CreateVisitLocators.ParamsTab.BENEFIT, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.FSIDIS_CONTAINER).click()
        # self.elements_are_visible(CreateVisitLocators.ParamsTab.FSIDIS, element=-1).click()

    def fill_additional_fields_patient(self):
        self.element_is_visible(CreateVisitLocators.TAB_ADDITIONAL).click()
        self.element_is_visible(CreateVisitLocators.AdditionalTab.CONSULTATION_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.AdditionalTab.CONSULTATION, element=-1).click()

    def fill_passport_registration_fields_patient(self):
        self.element_is_visible(CreateVisitLocators.TAB_PASSPORT_REGISTRATION).click()
        identifier_type = SystemDirectory.identifier_type[self.patient_info.identifier_type][1]
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_TYPE_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_TYPE,
                                  element=identifier_type).click()
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_SERIES).send_keys('_SERIES')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_NUMBER).send_keys('_NUMBER')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_ISSUED).send_keys('_ISSUED_BY')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_DATE_ISSUED).send_keys(12111996)
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_STATE_NUMBER).send_keys(13)
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_SUBJECT).send_keys('SUBJECT')
        self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.REGISTRATION_REGISTRATION_DISTRICT).send_keys('DISTRICT')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_CITY).send_keys('CITY')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_LOCALITY).send_keys('LOCALITY')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_STREET).send_keys('STREET')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_HOUSE).send_keys('HOUSE')
        self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_APARTMENT).send_keys(
            'APARTMENT')

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


class ComparisonVisitPage(CreateVisitPage):
    def compare_visit(self):
        compare_buttons = self.elements_are_visible(ComparisonVisitLocators.BUTTON_COMPARE)
        compare_buttons[0].click()
        self.waiting_for_notification('Сопоставление успешно выполнено.')


class CreateProtocolPage(VisitPage):
    def create_protocol(self):
        self.elements_are_visible(CreateProtocolLocators.BUTTONS_CREATE_PROTOCOL)[0].click()
        self.element_is_visible(CreateProtocolLocators.BUTTON_CLOSE_TEMPLATE_SELECTION).click()
        protocol_frame = self.element_is_present(CreateProtocolLocators.PROTOCOL_FRAME)
        self.driver.switch_to.frame(protocol_frame)
        description = self.element_is_visible(CreateProtocolLocators.DESCRIPTION_FIELD, True)
        conclusion = self.element_is_visible(CreateProtocolLocators.CONCLUSION_FIELD, True)
        recommendation = self.element_is_visible(CreateProtocolLocators.RECOMMENDATION_FIELD, True)
        self.click_and_send_keys(description, 'Описание')
        self.click_and_send_keys(conclusion, 'Заключение')
        self.click_and_send_keys(recommendation, 'Рекомендации')

    def save_protocol(self):
        self.driver.switch_to.default_content()
        self.element_is_visible(CreateProtocolLocators.BUTTON_EDITABLE, True).click()
        self.element_is_visible(CreateProtocolLocators.BUTTON_SAVE_PROTOCOL_AND_BACK, True).click()
