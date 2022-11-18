from selenium.webdriver.common.by import By


class PatientSearchPageLocators:
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input#lastName")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input#firstName")
    INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "input#middleName")
    INPUT_BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
    INPUT_SNILS = (By.CSS_SELECTOR, "input#snils")
    INPUT_POLIS = (By.CSS_SELECTOR, "input#polis")
    TBODY_PATIENTS = (By.CSS_SELECTOR, "table.table.table-bordered.table-condensed>tbody")
    PATIENT = (By.CSS_SELECTOR, "table.table.table-bordered.table-condensed>tbody>tr:nth-child(1)>td")
    MODIFY_PATIENT = (By.CSS_SELECTOR,
                      "table.table.table-bordered.table-condensed>tbody>tr:nth-child(1)>td>a:nth-child(1)>i.fa.fa-pencil")


class PatientPageLocators:
    TAB_DIAGNOSTIC_HISTORY = (By.CSS_SELECTOR, "a#patient-tabs-tab-diagnosticHistory")
    TAB_EDIT = (By.CSS_SELECTOR, "a#patient-tabs-tab-edit")

    class DiagnosticHistoryTab:
        pass

    class EditTab:
        INPUT_LAST_NAME = (By.CSS_SELECTOR, "input#lastName")
        INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input#firstName")
        INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "input#middleName")
        INPUT_BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
        SEX_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div")
        SEX = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div div[tabindex='-1']")
        SEX_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='sex']+div>div>div>div.react-select__single-value")
        INPUT_SNILS = (By.CSS_SELECTOR, "label.control-label[for='snils']+input.form-control")
        INPUT_POLIS = (By.CSS_SELECTOR, "input#polis_number")
        INPUT_ALTERNATE_ID = (By.CSS_SELECTOR, "input#alternateId")
        SAVE_BUTTON = (By.CSS_SELECTOR, "button#save")
        SAVE_AND_CONTINUE = (By.CSS_SELECTOR, "button#save-and-continue")
