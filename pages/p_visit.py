from data.data import SystemDirectory
from generator.generator import generated_person
from pages.p_authorization import AuthorizationPage
from locators.l_visit import VisitPageLocators as VisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from locators.l_visit import BindVisitPageLocators as BindVisitLocators
from locators.l_visit import ProtocolPageLocators as ProtocolLocators
from locators.l_visit import CreateProtocolPageLocators as CreateProtocolLocators


class VisitPage(AuthorizationPage):
    patient_info = next(generated_person())

    def go_to_create_visit(self):
        button_create_visit = self.element_is_visible(VisitLocators.CREATE_VISIT)
        self.get_request_href_and_click(button_create_visit)

    def open_visit(self, protocol: str):
        """protocol: present, editable, completed, missing, ignore"""
        match protocol:
            case 'present':
                visit = self.elements_are_visible(VisitLocators.PATIENTS_PRESENT_PROTOCOL_STUDY, element=0)
            case 'editable':
                visit = self.elements_are_visible(VisitLocators.PATIENTS_EDITABLE_PROTOCOL_STUDY, element=0)
            case 'completed':
                visit = self.elements_are_visible(VisitLocators.PATIENTS_COMPLETED_PROTOCOL_STUDY, element=0)
            case 'missing':
                visit = self.elements_are_visible(VisitLocators.PATIENTS_MISSING_PROTOCOL_STUDY, element=0)
            case 'ignore':
                visit = self.elements_are_visible(VisitLocators.PATIENTS_STUDY, element=0)
            case _:
                return 'Incorrect protocol'
        self.get_request_href_and_click(visit)

    def refresh_study_page(self):
        self.element_is_visible(VisitLocators.REFRESH_STUDY_PAGE)
        self.element_is_clickable(VisitLocators.REFRESH_STUDY_PAGE).click()

    def check_result_created_visit(self):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        patient = self.elements_are_visible(VisitLocators.PATIENTS_LIST)[0].text
        patient_birthday = self.elements_are_visible(VisitLocators.PATIENTS_BIRTHDAY)[0].text
        patient_birthday = patient_birthday.split()[0]
        return patient, patient_birthday


class CreateVisitPage(VisitPage):

    def fill_base_fields_patient(self):
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

        self.element_is_not_visible(self.Locators.LOADING_BAR)
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_visible(CreateVisitLocators.BaseTab.EXTERNAL_ID).send_keys('PATIENT_ID')
        self.element_is_visible(CreateVisitLocators.BaseTab.POLIS_OMS).send_keys('PATIENT_POLIS_OMS')
        self.element_is_visible(CreateVisitLocators.BaseTab.SNILS).send_keys(11223344595)
        self.element_is_visible(CreateVisitLocators.BaseTab.FULL_NAME).send_keys(full_name)
        self.element_is_visible(CreateVisitLocators.BaseTab.BIRTHDAY).send_keys(birthdate)
        self.element_is_visible(CreateVisitLocators.BaseTab.SEX_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.SEX, element=sex).click()
        self.element_is_visible(CreateVisitLocators.BaseTab.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(CreateVisitLocators.BaseTab.EMAIL).send_keys(email)
        self.element_is_visible(CreateVisitLocators.BaseTab.ALLERGY_TYPE_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.BaseTab.ALLERGY_TYPE, element=allergy_type).click()
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
        insurance_company = SystemDirectory.insurance_company[self.patient_info.insurance_company][1]
        self.element_is_visible(CreateVisitLocators.TAB_PARAMS).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_COMPANY_CONTAINER).click()
        self.elements_are_visible(CreateVisitLocators.ParamsTab.INSURANCE_COMPANY, element=insurance_company).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_CONTRACT).send_keys('_INSURANCE_CONTRACT')
        self.element_is_visible(CreateVisitLocators.ParamsTab.POLIS_NUMBER).send_keys('_PATIENT_POLIS')
        self.element_is_visible(CreateVisitLocators.ParamsTab.MEDICAL_DIAGNOSIS).send_keys('MEDICAL_DIAGNOSIS')
        self.element_is_visible(CreateVisitLocators.ParamsTab.ALTERNATE_ID).send_keys('PATIENT_ALTER_ID')
        self.element_is_visible(CreateVisitLocators.ParamsTab.HEIGHT).send_keys(180)
        self.element_is_visible(CreateVisitLocators.ParamsTab.WEIGHT).send_keys(80)
        self.element_is_visible(CreateVisitLocators.ParamsTab.FILM_COUNT).send_keys(3)
        self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_SIGN_CONTAINER).click()
        if not self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_SIGN_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.FLU_SIGN, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE_CONTAINER).click()
        if not self.element_is_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.FLU_PURPOSE, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.REF_ID).send_keys('REF_ID')
        self.element_is_visible(CreateVisitLocators.ParamsTab.REF_DATE).send_keys(12112022)
        self.element_is_visible(CreateVisitLocators.ParamsTab.DIRECTION_TYPE_CONTAINER).click()
        if not self.element_is_visible(CreateVisitLocators.ParamsTab.DIRECTION_TYPE_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.DIRECTION_TYPE, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.BENEFIT_CONTAINER).click()
        if not self.element_is_visible(CreateVisitLocators.ParamsTab.BENEFIT_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.BENEFIT, element=-1).click()
        self.element_is_visible(CreateVisitLocators.ParamsTab.FSIDIS_CONTAINER).click()
        if not self.element_is_visible(CreateVisitLocators.ParamsTab.FSIDIS_NO_DATE, return_false=True):
            self.elements_are_visible(CreateVisitLocators.ParamsTab.FSIDIS, element=-1).click()

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

    def fill_all_fields(self):
        entered_data = self.fill_base_fields_patient()
        self.fill_params_fields_patient()
        self.fill_additional_fields_patient()
        self.fill_passport_registration_fields_patient()
        return entered_data

    def save_visit(self, action: str):
        """action: continue, close, create, bind, bind_and_create"""
        match action:
            case 'continue':
                locator = CreateVisitLocators.BTN_SAVE_AND_CONTINUE
            case 'close':
                locator = CreateVisitLocators.BTN_SAVE_AND_CLOSE
            case 'create':
                locator = CreateVisitLocators.BTN_SAVE_AND_CREATE
            case 'bind':
                locator = CreateVisitLocators.BTN_SAVE_AND_BIND
            case 'bind_and_create':
                locator = CreateVisitLocators.BTN_SAVE_AND_BIND_AND_CREATE
            case _:
                return 'Incorrect action'
        self.element_is_visible(locator).click()

    def delete_visit(self):
        self.element_is_visible(CreateVisitLocators.BTN_DELETE).click()
        self.element_is_visible(CreateVisitLocators.REASON_FOR_DELETE).send_keys('Reason for delete')
        self.element_is_visible(CreateVisitLocators.BTN_MODAL_DELETE).click()
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_not_visible(self.Locators.LOADING_BAR)

    def delete_protocol(self):
        self.element_is_visible(CreateVisitLocators.TAB_CLINICAL_DOCUMENTS).click()
        self.element_is_visible(CreateVisitLocators.ClinicalDocumentsTab.PROTOCOL_DELETE).click()
        self.element_is_visible(CreateVisitLocators.BTN_MODAL_DELETE_NO)
        self.element_is_visible(CreateVisitLocators.BTN_MODAL_DELETE_YES).click()
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_not_visible(CreateVisitLocators.ClinicalDocumentsTab.PROTOCOL_DELETE)


class BindVisitPage(CreateVisitPage):
    def bind_visit(self):
        bind_buttons = self.elements_are_visible(BindVisitLocators.BTN_COMPARE)
        bind_buttons[0].click()
        self.waiting_for_notification('Сопоставление успешно выполнено.')


class ProtocolPage(VisitPage):
    def return_protocol_to_editable(self):
        self.elements_are_visible(VisitLocators.VIEW_PROTOCOL, element=0).click()
        self.element_is_visible(ProtocolLocators.BTN_RETURN_TO_EDITABLE).click()
        self.waiting_for_notification('Документ возвращен в режим редактирования.')

    def close_protocol(self):
        self.element_is_visible(ProtocolLocators.BTN_CLOSE)


class CreateProtocolPage(CreateVisitPage):
    def create_protocol(self, site: str):
        """site: visit_page, reg_form, tab_doc"""
        match site:
            case 'visit_page':
                self.elements_are_visible(VisitLocators.CREATE_PROTOCOL, element=0).click()
            case 'reg_form':
                self.open_visit('missing')
                self.element_is_visible(CreateVisitLocators.BTN_CREATE_PROTOCOL).click()
            case 'tab_doc':
                self.open_visit('missing')
                self.element_is_visible(CreateVisitLocators.TAB_CLINICAL_DOCUMENTS).click()
                self.element_is_visible(CreateVisitLocators.ClinicalDocumentsTab.PROTOCOL_CREATE).click()
            case _:
                return 'Incorrect site'
        self.element_is_visible(CreateProtocolLocators.BTN_CLOSE_TEMPLATE_SELECTION).click()
        protocol_frame = self.element_is_present(CreateProtocolLocators.PROTOCOL_FRAME)
        self.driver.switch_to.frame(protocol_frame)
        description = self.element_is_visible(CreateProtocolLocators.DESCRIPTION_FIELD)
        conclusion = self.element_is_visible(CreateProtocolLocators.CONCLUSION_FIELD)
        recommendation = self.element_is_visible(CreateProtocolLocators.RECOMMENDATION_FIELD)
        self.click_and_send_keys(description, 'Описание')
        self.click_and_send_keys(conclusion, 'Заключение')
        self.click_and_send_keys(recommendation, 'Рекомендации')

    def save_protocol(self):
        self.driver.switch_to.default_content()
        if not self.element_is_not_visible(CreateProtocolLocators.BTN_SAVE_PROTOCOL_AND_CONTINUE, return_false=True):
            self.element_is_visible(CreateProtocolLocators.BTN_EDITABLE).click()
        self.element_is_visible(CreateProtocolLocators.BTN_SAVE_PROTOCOL_AND_CLOSE).click()
        self.waiting_for_notification('Данные сохранены.')
        if self.element_is_visible(ProtocolLocators.MODAL_CONTENT, return_false=True):
            self.sign_protocol()

    def sign_protocol(self):
        self.element_is_visible(ProtocolLocators.SIGN_CONTAINER).click()
        self.elements_are_visible(ProtocolLocators.SIGN, element=-1).click()
        self.element_is_visible(ProtocolLocators.BTN_SIGN).click()
        self.waiting_for_notification('Документ подписан.')
