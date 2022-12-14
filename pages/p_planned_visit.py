from pages.p_main_content import MainContentPage
from locators.l_planned_visit import PlannedVisitPageLocators as PlannedVisitLocators
from locators.l_planned_visit import CreatePlannedVisitPageLocators as CreatePlannedVisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from generator.generator import generated_person
from data.data import SystemDirectory


class PlannedVisitPage(MainContentPage):
    patient_info = next(generated_person())

    def get_planned_visit(self):
        name = f'{self.patient_info.last_name} {self.patient_info.first_name[0]}. {self.patient_info.middle_name[0]}.'
        birthdate = f'{self.patient_info.birth_day}.{self.patient_info.birth_month}.{self.patient_info.birth_year}'
        cito = True if self.patient_info.is_cito != 'R' else False
        sex = SystemDirectory.sex[self.patient_info.sex][0]
        phone_number = self.patient_info.phone_number
        phone_number = f'{phone_number[0:2]} {phone_number[2:5]} {phone_number[5:8]}-{phone_number[8:10]}-{phone_number[10:]}'
        locator = PlannedVisitLocators.get_planned_visit_locator(cito, name, sex, birthdate,
                                                                 'Спиральная компьютерная томография головы',
                                                                 comment='COMMENT', number=phone_number)
        return True if self.element_is_visible(locator, return_false=True) else False

    def open_create_planned_visit(self):
        button_create_planned_visit = self.element_is_visible(PlannedVisitLocators.BUTTON_REGISTER_PLANNED_VISIT)
        self.get_request_href_and_click(button_create_planned_visit)


class CreatePlannedVisitPage(PlannedVisitPage):
    def check_base_fields(self):
        self.element_is_not_visible(self.Locators.BLOCK_PAGE)
        self.element_is_visible(CreateVisitLocators.TAB_BASE).click()
        full_name = f'{self.patient_info.last_name} {self.patient_info.first_name} {self.patient_info.middle_name}'
        birthdate = f'{self.patient_info.birth_year}-{self.patient_info.birth_month}-{self.patient_info.birth_day}'
        sex = SystemDirectory.sex[self.patient_info.sex][0]
        allergy_type = SystemDirectory.allergy_type[self.patient_info.allergy_type][0]
        treatment_case = SystemDirectory.treatment_case[self.patient_info.treatment_case][0]
        patient_class = SystemDirectory.patient_class[self.patient_info.patient_class][0]
        is_cito = SystemDirectory.is_cito[self.patient_info.is_cito][0]
        assert self.element_is_visible(CreateVisitLocators.BaseTab.EXTERNAL_ID).get_attribute('value') == 'PATIENT_ID'
        assert self.element_is_visible(CreatePlannedVisitLocators.POLIS_OMS).get_attribute(
            'value') == 'PATIENT_POLIS_OMS'
        assert self.element_is_visible(CreatePlannedVisitLocators.SNILS).get_attribute('value') == '112-233-445 95'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.FULL_NAME).get_attribute('value') == full_name
        assert self.element_is_visible(CreateVisitLocators.BaseTab.BIRTHDAY).get_attribute('value') == birthdate
        assert self.element_is_visible(CreateVisitLocators.BaseTab.SEX_SELECT_VALUE).text == sex
        assert self.element_is_visible(CreateVisitLocators.BaseTab.PHONE_NUMBER).get_attribute('value').replace(' ',
                                                                                                                '') == self.patient_info.phone_number
        assert self.element_is_visible(CreateVisitLocators.BaseTab.EMAIL).get_attribute(
            'value') == self.patient_info.email
        assert self.element_is_visible(CreateVisitLocators.BaseTab.ALLERGY_TYPE_SELECT_VALUE).text == allergy_type
        assert self.element_is_visible(CreateVisitLocators.BaseTab.TREATMENT_CASE_SELECT_VALUE).text == treatment_case
        assert self.element_is_visible(CreateVisitLocators.BaseTab.PATIENT_CLASS_SELECT_VALUE).text == patient_class
        assert self.element_is_visible(CreateVisitLocators.BaseTab.OUTPATIENT_CARD_NUMBER).get_attribute(
            'value') == 'OUTPATIENT_CARD_NUMBER'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.CASE_HISTORY_NUMBER).get_attribute(
            'value') == 'CASE_HISTORY_NUMBER'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.REF_DEPARTMENT).get_attribute(
            'value') == 'REF_DEPARTMENT'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.REF_DOCTOR).get_attribute('value') == 'REF_DOCTOR'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.SOURCE_FINANCING_SELECT_VALUE).text == 'ДМС'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.PURPOSE).get_attribute('value') == 'PURPOSE'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.DIAGNOSES_MKB_SELECTED_NODES).get_attribute(
            'data-id') == 'M19.0'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.COMMENT).text == 'COMMENT'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.IS_CITO_SELECT_VALUE).text == is_cito

    def check_params_fields(self):
        self.element_is_visible(CreateVisitLocators.TAB_PARAMS).click()
        insurance_company = SystemDirectory.insurance_company[self.patient_info.insurance_company][0]
        assert self.element_is_visible(
            CreateVisitLocators.ParamsTab.INSURANCE_COMPANY_SELECT_VALUE).text == insurance_company
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_CONTRACT).get_attribute(
            'value') == 'INSURANCE_CONTRACT'
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.POLIS_NUMBER).get_attribute(
            'value') == '_PATIENT_POLIS'
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.ALTERNATE_ID).get_attribute(
            'value') == 'PATIENT_ALTER_ID'

    def check_additional_fields(self):
        self.element_is_visible(CreateVisitLocators.TAB_ADDITIONAL).click()
        self.element_is_visible(CreateVisitLocators.AdditionalTab.CONSULTATION_CONTAINER)

    def check_passport_registration_fields(self):
        self.element_is_visible(CreateVisitLocators.TAB_PASSPORT_REGISTRATION).click()
        identifier_type = SystemDirectory.identifier_type[self.patient_info.identifier_type][0]
        print(identifier_type)
        identifier_type_element = self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_TYPE_SELECT_VALUE).text
        print(identifier_type_element)
        assert identifier_type_element == identifier_type
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_SERIES).get_attribute(
            'value') == '_SERIES'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_NUMBER).get_attribute(
            'value') == '_NUMBER'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_ISSUED).get_attribute(
            'value') == '_ISSUED_BY'
        assert self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_DATE_ISSUED).get_attribute(
            'value') == '1996-11-12'
        assert self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.REGISTRATION_STATE_NUMBER).get_attribute(
            'value') == '13'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_SUBJECT).get_attribute(
            'value') == 'SUBJECT'
        assert self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.REGISTRATION_REGISTRATION_DISTRICT).get_attribute(
            'value') == 'DISTRICT'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_CITY).get_attribute(
            'value') == 'CITY'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_LOCALITY).get_attribute(
            'value') == 'LOCALITY'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_STREET).get_attribute(
            'value') == 'STREET'
        assert self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.REGISTRATION_HOUSE).get_attribute(
            'value') == 'HOUSE'
        assert self.element_is_visible(
            CreateVisitLocators.PassportRegistrationTab.REGISTRATION_APARTMENT).get_attribute(
            'value') == 'APARTMENT'

    def check_all_fields(self):
        self.check_base_fields()
        self.check_params_fields()
        self.check_additional_fields()
        self.check_passport_registration_fields()

    def register_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.BaseTab.DEVICE_CONTAINER)
        self.element_is_visible(CreateVisitLocators.BTN_SAVE_AND_CONTINUE).click()
        self.element_is_not_visible(self.Locators.LOADING_BAR)

    def delete_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.BTN_DELETE).click()
        self.element_is_visible(CreateVisitLocators.REASON_FOR_DELETE).send_keys('Reason to delete')
        self.element_is_visible(CreateVisitLocators.BTN_MODAL_DELETE).click()
        self.element_is_not_visible(self.Locators.LOADING_BAR)
