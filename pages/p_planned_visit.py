from pages.p_authorization import AuthorizationPage
from locators.l_planned_visit import PlannedVisitPageLocators as PlannedVisitLocators
from locators.l_planned_visit import CreatePlannedVisitPageLocators as CreatePlannedVisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from generator.generator import generated_person
from data.data import SystemDirectory


class PlannedVisitPage(AuthorizationPage):
    def check_list_planned_visits(self):
        self.element_is_visible(PlannedVisitLocators.TBODY_PLANNED_VISITS)
        planned_visit = self.elements_are_visible(PlannedVisitLocators.PLANNED_VISIT)
        print(planned_visit[3].text, planned_visit[5].text)

    def go_to_create_planned_visit(self):
        button_create_planned_visit = self.element_is_visible(PlannedVisitLocators.BUTTON_REGISTER_PLANNED_VISIT)
        link_href = button_create_planned_visit.get_attribute('href')
        request = self.get_request(link_href)
        if request.status_code == 200:
            button_create_planned_visit.click()
        assert link_href in self.current_url()


class CreatePlannedVisitPage(PlannedVisitPage):
    patient_info = next(generated_person())

    def check_base_planned_visit(self):
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        self.element_is_visible(CreateVisitLocators.TAB_BASE).click()
        full_name = f'{self.patient_info.last_name} {self.patient_info.first_name} {self.patient_info.middle_name}'
        email = self.patient_info.email
        phone_number = self.patient_info.phone_number
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
                                                                                                                '') == phone_number
        assert self.element_is_visible(CreateVisitLocators.BaseTab.EMAIL).get_attribute('value') == email
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
        # assert self.element_is_visible(CreateVisitLocators.BaseTab.PURPOSE).get_attribute('value') == 'PURPOSE'
        # МКБ ------
        assert self.element_is_visible(CreateVisitLocators.BaseTab.COMMENT).text == 'COMMENT'
        assert self.element_is_visible(CreateVisitLocators.BaseTab.IS_CITO_SELECT_VALUE).text == is_cito

    def check_params_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.TAB_PARAMS).click()
        # insurance_company = self.patient_info.insurance_company
        self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_COMPANY_CONTAINER)
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.INSURANCE_CONTRACT).get_attribute(
            'value') == '_INSURANCE_CONTRACT'
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.POLIS_NUMBER).get_attribute(
            'value') == '_PATIENT_POLIS'
        assert self.element_is_visible(CreateVisitLocators.ParamsTab.ALTERNATE_ID).get_attribute(
            'value') == 'PATIENT_ALTER_ID'

    def check_additional_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.TAB_ADDITIONAL).click()
        self.element_is_visible(CreateVisitLocators.AdditionalTab.CONSULTATION_CONTAINER)

    def check_passport_registration_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.TAB_PASSPORT_REGISTRATION).click()
        identifier_type = SystemDirectory.identifier_type[self.patient_info.identifier_type][0]
        print(identifier_type)
        identifier_type_element = self.element_is_visible(CreateVisitLocators.PassportRegistrationTab.IDENTIFIER_TYPE_SELECT_VALUE).text
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

    def register_a_planned_visit(self):
        self.element_is_visible(CreateVisitLocators.BaseTab.DEVICE_CONTAINER)
        self.element_is_visible(CreateVisitLocators.BTN_SAVE_AND_CONTINUE, True).click()
