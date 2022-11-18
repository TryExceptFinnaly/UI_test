from selenium.webdriver.common.by import By


class UnregStudiesPageLocators:
    TBODY_UNREG_STUDIES = (By.CSS_SELECTOR, "table.table.table-bordered.table-condensed.unreg-list-table>tbody")
    UNREG_STUDY = (
        By.CSS_SELECTOR, "table.table.table-bordered.table-condensed.unreg-list-table>tbody>tr:nth-child(1)>td")
