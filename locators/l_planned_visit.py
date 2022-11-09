from selenium.webdriver.common.by import By


class PlannedVisitPageLocators:
    TBODY_PLANNED_VISITS = (By.CSS_SELECTOR, 'table.table.table-bordered.table-condensed.planned-list-table>tbody')
    PLANNED_VISIT = (By.CSS_SELECTOR,
                     'table.table.table-bordered.table-condensed.planned-list-table>tbody>tr:nth-child(1)>td')
    BUTTON_REGISTER_PLANNED_VISIT = (By.CSS_SELECTOR,
                                     'table.table.table-bordered.table-condensed.planned-list-table>tbody>tr:nth-child(1)>td>a:nth-child(2)')
    DEVICE_CONTAINER = (By.CSS_SELECTOR, 'label[for="device"]+div>div>div.react-select__value-container.react-select__value-container--has-value')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'div.pull-right>div.btn-group>button:nth-child(3)')