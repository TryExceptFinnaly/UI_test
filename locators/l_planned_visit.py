from selenium.webdriver.common.by import By


class PlannedVisitPageLocators:
    TBODY_PLANNED_VISITS = (By.CSS_SELECTOR, 'table.table.table-bordered.table-condensed.planned-list-table>tbody')
    PLANNED_VISIT = (By.CSS_SELECTOR,
                     'table.table.table-bordered.table-condensed.planned-list-table>tbody>tr:nth-child(1)>td')
    BUTTON_REGISTER_PLANNED_VISIT = (By.CSS_SELECTOR,
                                     'table.table.table-bordered.table-condensed.planned-list-table>tbody>tr:nth-child(1)>td>a:nth-child(2)')


class CreatePlannedVisitPageLocators:
    POLIS_OMS = (By.CSS_SELECTOR, "input#patient_polis_number")
    SNILS = (By.CSS_SELECTOR, "label.control-label[for='snils']+input.form-control")
