from pages.p_authorization import AuthorizationPage
from locators.l_planned_visit import PlannedVisitPageLocators as PlannedVisitLocators
from locators.l_visit import CreateVisitPageLocators as CreateVisitLocators
from generator.generator import generated_person
from data.data import SystemDirectory


class PlannedVisitPage(AuthorizationPage):
    def check_list_planned_visits(self):
        self.element_is_visible(PlannedVisitLocators.TBODY_PLANNED_VISITS)
        planned_visit = self.elements_are_visible(PlannedVisitLocators.PLANNED_VISIT)
        print(planned_visit[3].text, planned_visit[5].text)

    def check_data_planned_visit(self):
        self.element_is_visible(PlannedVisitLocators.BUTTON_REGISTER_PLANNED_VISIT).click()
        self.element_is_not_visible(CreateVisitLocators.BLOCK_PAGE)
        patient_info = next(generated_person())
        full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
        email = patient_info.email
        phone_number = patient_info.phone_number
        birthdate = f'{patient_info.birth_year}-{patient_info.birth_month}-{patient_info.birth_day}'
        sex = SystemDirectory.sex[patient_info.sex][0]
        allergy_type = SystemDirectory.allergy_type[patient_info.allergy_type][0]
        treatment_case = SystemDirectory.treatment_case[patient_info.treatment_case][0]
        patient_class = SystemDirectory.patient_class[patient_info.patient_class][0]
        is_cito = SystemDirectory.is_cito[patient_info.is_cito][0]
        assert self.element_is_visible(CreateVisitLocators.EXTERNAL_ID).get_attribute('value') == 'PATIENT_ID'
        assert self.element_is_visible(PlannedVisitLocators.POLIS_OMS).get_attribute('value') == 'PATIENT_POLIS_OMS'
        assert self.element_is_visible(PlannedVisitLocators.SNILS).get_attribute('value') == '148-587-332 10'
        assert self.element_is_visible(CreateVisitLocators.FULL_NAME).get_attribute('value') == full_name
        assert self.element_is_visible(CreateVisitLocators.BIRTHDAY).get_attribute('value') == birthdate
        assert self.element_is_visible(CreateVisitLocators.SEX_SELECT_VALUE).text == sex
        assert self.element_is_visible(CreateVisitLocators.PHONE_NUMBER).get_attribute('value').replace(' ',
                                                                                                        '') == phone_number
        assert self.element_is_visible(CreateVisitLocators.EMAIL).get_attribute('value') == email
        assert self.element_is_visible(CreateVisitLocators.ALLERGY_TYPE_SELECT_VALUE).text == allergy_type
        assert self.element_is_visible(CreateVisitLocators.TREATMENT_CASE_SELECT_VALUE).text == treatment_case
        assert self.element_is_visible(CreateVisitLocators.PATIENT_CLASS_SELECT_VALUE).text == patient_class
        assert self.element_is_visible(CreateVisitLocators.OUTPATIENT_CARD_NUMBER).get_attribute(
            'value') == 'OUTPATIENT_CARD_NUMBER'
        assert self.element_is_visible(CreateVisitLocators.CASE_HISTORY_NUMBER).get_attribute(
            'value') == 'CASE_HISTORY_NUMBER'
        assert self.element_is_visible(CreateVisitLocators.REF_DEPARTMENT).get_attribute('value') == 'REF_DEPARTMENT'
        assert self.element_is_visible(CreateVisitLocators.REF_DOCTOR).get_attribute('value') == 'REF_DOCTOR'
        assert self.element_is_visible(CreateVisitLocators.SOURCE_FINANCING_SELECT_VALUE).text == 'ДМС'
        # assert self.element_is_visible(CreateVisitLocators.PURPOSE).get_attribute('value') == 'PURPOSE'
        # МКБ ------
        assert self.element_is_visible(CreateVisitLocators.COMMENT).text == 'COMMENT'
        assert self.element_is_visible(CreateVisitLocators.IS_CITO_SELECT_VALUE).text == is_cito

    def register_a_planned_visit(self):
        self.element_is_visible(PlannedVisitLocators.BUTTON_REGISTER_PLANNED_VISIT).click()
        self.element_is_visible(CreateVisitLocators.DEVICE_CONTAINER)
        self.element_is_visible(PlannedVisitLocators.SAVE_BUTTON, True).click()
