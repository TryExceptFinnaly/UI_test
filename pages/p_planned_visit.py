from pages.p_authorization import AuthorizationPage
from locators.l_planned_visit import PlannedVisitPageLocators as PlannedVisitLocators
from locators.l_visit import CreateVisitPageLocators as RegFormLocators


class PlannedVisitPage(AuthorizationPage):
    def check_list_planned_visits(self):
        self.element_is_visible(PlannedVisitLocators.TBODY_PLANNED_VISITS)
        planned_visit = self.elements_are_visible(PlannedVisitLocators.PLANNED_VISIT)
        print(planned_visit[3].text, planned_visit[5].text)

    def register_a_planned_visit(self):
        self.element_is_visible(PlannedVisitLocators.BUTTON_REGISTER_PLANNED_VISIT).click()
        self.element_is_visible(RegFormLocators.DEVICE_CONTAINER)
        self.element_is_visible(PlannedVisitLocators.SAVE_BUTTON, True).click()

