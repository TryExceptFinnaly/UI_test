from pages.p_authorization import AuthorizationPage
from locators.l_unreg_studies import UnregStudiesPageLocators as UnregStudiesLocators


class UnregStudiesPage(AuthorizationPage):
    def check_list_unreg_studies(self):
        self.element_is_visible(UnregStudiesLocators.TBODY_UNREG_STUDIES)
        unreg_study = self.elements_are_visible(UnregStudiesLocators.UNREG_STUDY)
        return (unreg_study[4].text, unreg_study[5].text)
