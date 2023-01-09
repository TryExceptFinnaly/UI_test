from generator.generator import generated_person
from pages.p_main_content import MainContentPage
from locators.l_unreg_studies import UnregStudiesPageLocators as UnregStudiesLocators


class UnregStudiesPage(MainContentPage):
    patient_info = next(generated_person())
    patient_info.full_name = f'{patient_info.last_name} {patient_info.first_name} {patient_info.middle_name}'
    patient_info.birthdate = f'{patient_info.birth_day}.{patient_info.birth_month}.{patient_info.birth_year}'

    def refresh_page(self):
        self.element_is_not_visible(self.Locators.LOADING_BAR)
        self.element_is_visible(UnregStudiesLocators.REFRESH_PAGE)
        self.element_is_clickable(UnregStudiesLocators.REFRESH_PAGE).click()
        self.element_is_visible(self.Locators.LOADING_BAR)
        self.element_is_not_visible(self.Locators.LOADING_BAR)

    def get_unreg_study(self):
        locator = UnregStudiesLocators.get_unreg_study_locator(self.patient_info.full_name,
                                                               self.patient_info.birthdate,
                                                               self.patient_info.sex, 'PATIENT_ID', 'NAME_STUDY',
                                                               'PART_OF_THE_BODY', 'ГБУЗ "Старая Руса"',
                                                               modality='CT')
        unreg_study = self.elements_are_visible(locator, return_false=True)
        return unreg_study if unreg_study else False

    def delete_unreg_study(self, unreg_study):
        unreg_study = unreg_study[0].find_elements(*UnregStudiesLocators.BTN_DELETE)
        unreg_study[0].click()
        self.element_is_visible(UnregStudiesLocators.BTN_MODAL_DELETE_YES).click()
