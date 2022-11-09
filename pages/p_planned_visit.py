from pages.p_authorization import AuthorizationPage
from locators.l_planned_visit import PlannedVisitPageLocators


class PlannedVisitPage(AuthorizationPage):
    locators = PlannedVisitPageLocators()

    def check_list_planned_visits(self):
        self.element_is_visible(self.locators.TBODY_PLANNED_VISITS)
        planned_visit = self.elements_are_visible(self.locators.PLANNED_VISIT)
        print(planned_visit[3].text, planned_visit[5].text)

    def register_a_planned_visit(self):
        self.element_is_visible(self.locators.BUTTON_REGISTER_PLANNED_VISIT).click()
        self.element_is_visible(self.locators.DEVICE_CONTAINER)
        self.element_is_visible(self.locators.SAVE_BUTTON, True).click()

