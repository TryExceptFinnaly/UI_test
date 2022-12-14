from selenium.webdriver.common.by import By


class VisitPageLocators:
    STUDY_PAGE = (By.CSS_SELECTOR, 'div.pull-left>h1.pull-left')
    CREATE_VISIT = (By.CSS_SELECTOR, "a.btn.btn-primary[href='/visit/create/']")
    CREATE_PROTOCOL = (By.XPATH, "//tr/td/a[@class='no-underline']/i[@class='fa fa-plus']")
    VIEW_PROTOCOL = (By.XPATH, "//tr/td/a[@class='no-underline']/i[@class='fa fa-file-text-o']")
    EDIT_PROTOCOL = (By.XPATH, "//tr/td/a[@class='no-underline']/i[@class='fa fa-pencil']")
    SEARCH_PATIENT = (
        By.XPATH, "//tr[td[span[br][text()='BIRTHDATE']]][td[a[text()='NAME']]][td[ul[li[a[@href][text()='STUDY']]]]]")
    PATIENTS_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>a[href^='/share/visits/']")
    PATIENTS_BIRTHDAY = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>span:has(br)")
    #
    PATIENTS_STUDY = (By.XPATH, "//tr/td//a[not(@class)][contains(@href,'/visit/')]")
    PATIENTS_MISSING_PROTOCOL_STUDY = (By.XPATH,
                                       "//tr[td[a[i[@class='fa fa-plus']]]]//a[not(@class)][contains(@href,'/visit/')]")
    PATIENTS_COMPLETED_PROTOCOL_STUDY = (By.XPATH,
                                         "//tr[td[a[i[@class='fa fa-file-text-o']]]]//a[not(@class)][contains(@href,'/visit/')]")
    PATIENTS_EDITABLE_PROTOCOL_STUDY = (By.XPATH,
                                        "//tr[td[a[i[@class='fa fa-pencil']]]]//a[not(@class)][contains(@href,'/visit/')]")
    PATIENTS_PRESENT_PROTOCOL_STUDY = (By.XPATH,
                                       "//tr[td[a[i[@class='fa fa-pencil' or @class='fa fa-file-text-o']]]]//a[not(@class)][contains(@href,'/visit/')]")
    PREFIX = '//tr'
    PREFIX_PRESENT_WLM = '//tr[td[5][div[text()="PACS"]]]'
    PREFIX_MISSING_WLM = '//tr[td[5][not(div[text()="PACS"])]]'
    PREFIX_PRESENT_IMAGE = '//tr[td[3][a]]'
    PREFIX_MISSING_IMAGE = '//tr[td[3][not(a)]]'
    #
    VIEW_IMAGE_VISIT = (By.XPATH, "//tr/td//i[@class='fa fa-picture-o']/..")
    REFRESH_STUDY_PAGE = (By.CSS_SELECTOR, "i.fa.fa-refresh")


class CreateVisitPageLocators:
    # TABS
    TAB_BASE = (By.CSS_SELECTOR, "a#regform-tabs-tab-base")
    TAB_PARAMS = (By.CSS_SELECTOR, "a#regform-tabs-tab-params")
    TAB_ADDITIONAL = (By.CSS_SELECTOR, "a#regform-tabs-tab-additional")
    TAB_PASSPORT_REGISTRATION = (By.CSS_SELECTOR, "a#regform-tabs-tab-passport-registration")
    TAB_CLINICAL_DOCUMENTS = (By.CSS_SELECTOR, "a#regform-tabs-tab-cdocuments")

    # MAIN
    BTN_SAVE_AND_CONTINUE = (By.CSS_SELECTOR, 'button[data-testid="btn-save-and-continue"]')
    BTN_SAVE_AND_CLOSE = (By.CSS_SELECTOR, 'button[data-testid="btn-save-and-close"]')
    BTN_SAVE_AND_CREATE = (By.CSS_SELECTOR, 'button[data-testid="btn-save-and-create"]')
    BTN_SAVE_AND_BIND = (By.CSS_SELECTOR, 'button[data-testid="btn-save-and-bind"]')
    BTN_SAVE_AND_BIND_AND_CREATE = (By.CSS_SELECTOR, 'button[data-testid="btn-save-and-bind-and-create"]')
    BTN_CREATE_PROTOCOL = (By.CSS_SELECTOR, 'button[data-testid="btn-create-protocol"]')
    BTN_DELETE = (By.CSS_SELECTOR, 'button[data-testid="btn-delete"]')
    REASON_FOR_DELETE = (By.CSS_SELECTOR, "textarea#description")
    BTN_MODAL_DELETE = (By.CSS_SELECTOR, "button#modal-action-delete")
    BTN_MODAL_DELETE_YES = (
        By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer>button.btn.btn-danger")
    BTN_MODAL_DELETE_NO = (
        By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer>button.btn.btn-default")

    class BaseTab:
        #   PERSON DATA
        EXTERNAL_ID = (By.CSS_SELECTOR, "input#external_id")
        POLIS_OMS = (By.CSS_SELECTOR,
                     "div.form-group>label.control-label[for='patient_polis_number']+div.btn-group.bootstrap-select.form-control.open>input.form-control[value]")
        SNILS = (By.CSS_SELECTOR,
                 "div.form-group>label.control-label[for='snils']+div.btn-group.bootstrap-select.form-control.open>input.form-control[value]")
        # SNILS = (By.XPATH,
        #          "//div[@id='regform-tabs-pane-base']//label[@for='snils']/following-sibling::div[@class='btn-group bootstrap-select form-control open']/input[@value]")
        FULL_NAME = (By.CSS_SELECTOR, "input#full_name")
        BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
        SEX_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='sex']+div.react-select-container")
        SEX = (By.CSS_SELECTOR,
               "div.form-group>label.control-label[for='sex']+div>div div.react-select__option[tabindex='-1']")
        SEX_SELECT_VALUE = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='sex']+div>div>div>div.react-select__single-value")
        PHONE_NUMBER = (By.CSS_SELECTOR, "input#phone_number")
        EMAIL = (By.CSS_SELECTOR, "input#email")
        ALLERGY_TYPE_CONTAINER = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='allergy_type']+div.react-select-container")
        ALLERGY_TYPE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='allergy_type']+div>div div.react-select__option[tabindex='-1']")
        ALLERGY_TYPE_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='allergy_type']+div>div>div>div.react-select__single-value")
        YEAR_DOSE = (By.CSS_SELECTOR, "input#year_dose[disabled]")
        #   DATA DIRECTION
        TREATMENT_CASE_CONTAINER = (By.CSS_SELECTOR,
                                    "div.form-group>label.control-label[for='treatment_case']+div.react-select-container")
        TREATMENT_CASE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='treatment_case']+div>div div.react-select__option[tabindex='-1']")
        TREATMENT_CASE_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='treatment_case']+div>div>div>div.react-select__single-value")
        PATIENT_CLASS_CONTAINER = (By.CSS_SELECTOR,
                                   "div.form-group>label.control-label[for='patient_class']+div.react-select-container")
        PATIENT_CLASS = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='patient_class']+div>div div.react-select__option[tabindex='-1']")
        PATIENT_CLASS_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='patient_class']+div>div>div>div.react-select__single-value")
        OUTPATIENT_CARD_NUMBER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='outpatient_card_number']+div>input.form-control")
        CASE_HISTORY_NUMBER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='case_history_number']+div>input.form-control")
        REF_DEPARTMENT = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='ref_department']+div>input.form-control")
        REF_DOCTOR = (By.CSS_SELECTOR, "div.form-group>label.control-label[for='ref_doctor']+div>input.form-control")
        SOURCE_FINANCING_CONTAINER = (By.CSS_SELECTOR,
                                      "div.form-group>label.control-label[for='source_financing']+div.react-select-container")
        SOURCE_FINANCING = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='source_financing']+div>div div.react-select__option[tabindex='-1']")
        SOURCE_FINANCING_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='source_financing']+div>div>div>div.react-select__single-value")
        PURPOSE = (By.CSS_SELECTOR, "div.form-group>label.control-label[for='purpose']+div>input.form-control")
        DIAGNOSES_MKB_CONTAINER = (By.CSS_SELECTOR, "div#diagnoses.jstree-widget")
        DIAGNOSES_MKB_SEARCH_INPUT = (By.CSS_SELECTOR, "div#diagnoses>div.jstree-widget-content>input")
        DIAGNOSES_MKB_SELECTED_NODES = (
            By.CSS_SELECTOR, "div#diagnoses>div.jstree-widget-field>div>ul>li>i.fa.fa-times")
        DIAGNOSES_MKB_NODES = (By.CSS_SELECTOR, "div#diagnoses>div.jstree-widget-content>div>ul>li.jstree-node")
        COMMENT = (By.CSS_SELECTOR, "textarea#comment")
        #   DATA STUDY
        DOCTOR_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='doctor']+div.react-select-container")
        ASSISTANT_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='assistant']+div.react-select-container")
        TYPES_OF_STUDY_CONTAINER = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='studies']+div.studies-field>span div.react-select__control")
        TYPE_OF_STUDY = (By.CSS_SELECTOR,
                         "div.form-group>label.control-label[for='studies']+div div.react-select__option[tabindex='-1']")
        TYPE_OF_STUDY_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='studies']+div div.react-select__multi-value__label")
        DEVICE_CONTAINER = (By.CSS_SELECTOR,
                            'label[for="device"]+div>div>div.react-select__value-container.react-select__value-container--has-value')
        CONTRAST_CONTAINER = (By.CSS_SELECTOR,
                              "div.form-group>label.control-label[for='contrast_enhancement']+div.react-select-container")
        CONTRAST = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='contrast_enhancement']+div>div div.react-select__option[tabindex='-1']")
        CONTRAST_VOLUME = (By.CSS_SELECTOR, "input#contrast_volume")
        DOSE_RG = (By.CSS_SELECTOR, "input#doseRG")
        DOSE = (By.CSS_SELECTOR, "input#dose[disabled]")
        IS_CITO_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='is_cito']+div.react-select-container")
        IS_CITO = (By.CSS_SELECTOR,
                   "div.form-group>label.control-label[for='is_cito']+div>div div.react-select__option[tabindex='-1']")
        IS_CITO_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='is_cito']+div>div>div>div.react-select__single-value")

    class ParamsTab:
        INSURANCE_COMPANY_CONTAINER = (By.CSS_SELECTOR,
                                       "div.form-group>label.control-label[for='insurance_company']+div.react-select-container")
        INSURANCE_COMPANY = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='insurance_company']+div>div div.react-select__option[tabindex='-1']")
        INSURANCE_COMPANY_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='insurance_company']+div>div>div>div.react-select__single-value")
        INSURANCE_CONTRACT = (By.CSS_SELECTOR, "input#insurance_contract")
        POLIS_NUMBER = (By.CSS_SELECTOR, "input#polis_number")
        MEDICAL_DIAGNOSIS = (By.CSS_SELECTOR, "input#medical_diagnosis")
        ALTERNATE_ID = (By.CSS_SELECTOR, "input#alternate_id")
        HEIGHT = (By.CSS_SELECTOR, "input#height")
        WEIGHT = (By.CSS_SELECTOR, "input#weight")
        FILM_COUNT = (By.CSS_SELECTOR, "input#film_count")
        FLU_SIGN_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='fluSign']+div.react-select-container")
        FLU_SIGN_NO_DATE = (By.CSS_SELECTOR,
                            "div.form-group>label.control-label[for='fluSign']+div>div>div>div.react-select__menu-notice.react-select__menu-notice--no-options")
        FLU_SIGN = (By.CSS_SELECTOR,
                    "div.form-group>label.control-label[for='fluSign']+div>div div.react-select__option[tabindex='-1']")
        FLU_PURPOSE_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='fluPurpose']+div.react-select-container")
        FLU_PURPOSE_NO_DATE = (By.CSS_SELECTOR,
                               "div.form-group>label.control-label[for='fluPurpose']+div>div>div>div.react-select__menu-notice.react-select__menu-notice--no-options")
        FLU_PURPOSE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='fluPurpose']+div>div div.react-select__option[tabindex='-1']")
        REF_ID = (By.CSS_SELECTOR, "input#ref_id")
        REF_DATE = (By.CSS_SELECTOR, "input#ref_date")
        DIRECTION_TYPE_CONTAINER = (By.CSS_SELECTOR,
                                    "div.form-group>label.control-label[for='direction_type']+div.react-select-container")

        DIRECTION_TYPE_NO_DATE = (By.CSS_SELECTOR,
                                  "div.form-group>label.control-label[for='direction_type']+div>div>div>div.react-select__menu-notice.react-select__menu-notice--no-options")
        DIRECTION_TYPE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='direction_type']+div>div div.react-select__option[tabindex='-1']")
        BENEFIT_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='benefit']+div.react-select-container")

        BENEFIT_NO_DATE = (By.CSS_SELECTOR,
                           "div.form-group>label.control-label[for='benefit']+div>div>div>div.react-select__menu-notice.react-select__menu-notice--no-options")
        BENEFIT = (By.CSS_SELECTOR,
                   "div.form-group>label.control-label[for='benefit']+div>div div.react-select__option[tabindex='-1']")
        FSIDIS_CONTAINER = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='fsidis']+div.react-select-container")

        FSIDIS_NO_DATE = (By.CSS_SELECTOR,
                          "div.form-group>label.control-label[for='fsidis']+div>div>div>div.react-select__menu-notice.react-select__menu-notice--no-options")
        FSIDIS = (By.CSS_SELECTOR,
                  "div.form-group>label.control-label[for='fsidis']+div>div div.react-select__option[tabindex='-1']")

    class AdditionalTab:
        CONSULTATION_CONTAINER = (By.CSS_SELECTOR,
                                  "div.form-group>div>label.control-label[for='customField23']+div.react-select-container")
        CONSULTATION = (
            By.CSS_SELECTOR,
            "div.form-group>div>label.control-label[for='customField23']+div>div div.react-select__option[tabindex='-1']")

    class PassportRegistrationTab:
        IDENTIFIER_TYPE_CONTAINER = (By.CSS_SELECTOR,
                                     "div.form-group>label.control-label[for='identifier_type']+div.react-select-container")
        IDENTIFIER_TYPE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='identifier_type']+div>div div.react-select__option[tabindex='-1']")
        IDENTIFIER_TYPE_SELECT_VALUE = (
            By.CSS_SELECTOR,
            "div.form-group>label.control-label[for='identifier_type']+div>div>div>div.react-select__single-value")
        IDENTIFIER_TYPE_ERROR = (By.XPATH, '//*[@id="regform-tabs-pane-passport-registration"]/div[1]/div[1]/div/span')
        IDENTIFIER_SERIES = (By.CSS_SELECTOR, "input#identifier_series")
        IDENTIFIER_NUMBER = (By.CSS_SELECTOR, "input#identifier_number")
        IDENTIFIER_ISSUED = (By.CSS_SELECTOR, "input#identifier_issued")
        IDENTIFIER_DATE_ISSUED = (By.CSS_SELECTOR, "input#identifier_date_issued")
        REGISTRATION_STATE_NUMBER = (By.CSS_SELECTOR, "input#registration_state_number")
        REGISTRATION_SUBJECT = (By.CSS_SELECTOR, "input#registration_subject")
        REGISTRATION_REGISTRATION_DISTRICT = (
            By.CSS_SELECTOR, "div.form-group>label.control-label[for='registration_district']+div>input")
        REGISTRATION_CITY = (By.CSS_SELECTOR, "input#registration_city")
        REGISTRATION_LOCALITY = (By.CSS_SELECTOR, "input#registration_locality")
        REGISTRATION_STREET = (By.CSS_SELECTOR, "input#registration_street")
        REGISTRATION_HOUSE = (By.CSS_SELECTOR, "input#registration_house")
        REGISTRATION_APARTMENT = (By.CSS_SELECTOR, "input#registration_apartment")

    class ClinicalDocumentsTab:
        PROTOCOL_DELETE = (
            By.XPATH,
            '//div[@id="regform-tabs-pane-cdocuments"]/table/tbody/tr[3]/td/div/a/i[@class="fa fa-trash"]')
        PROTOCOL_CREATE = (
            By.XPATH,
            '//div[@id="regform-tabs-pane-cdocuments"]/table/tbody/tr[3]/td/div/a/i[@class="fa fa-plus"]')


class ImageVisitPageLocators:
    BTN_DELETE = (By.XPATH, "//div[@class='pacs-image']//i[@class='fa fa-remove']/..")
    BTN_CLOSE_IMAGE_PAGE = (By.XPATH, "//div[@class='modal-content'][@role='document']//button[@class='close']")


class BindVisitPageLocators:
    BTN_COMPARE = (By.CSS_SELECTOR,
                   "div.table-responsive>table.table.table-bordered.table-condensed>tbody>tr>td>button.btn.btn-default")


class ProtocolPageLocators:
    MODAL_CONTENT = (By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content")
    SIGNED_PDF = (By.CSS_SELECTOR, "div.modal-content[role='document']>div.modal-body object[data*='/print_']")
    SIGN_CONTAINER = (
        By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer div.react-select-container")
    SIGN = (By.CSS_SELECTOR,
            "div[role='dialog']>div>div.modal-content>div.modal-footer div.react-select-container>div div.react-select__option[tabindex='-1']")
    BTN_SIGN = (By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer button.btn.btn-primary")
    BTN_RETURN_TO_EDITABLE = (By.CSS_SELECTOR,
                              "div[role='dialog']>div>div.modal-content>div.modal-footer>div>div.pull-left>button.btn.btn-default")
    BTN_CLOSE = (By.CSS_SELECTOR,
                 "div[role='dialog']>div>div.modal-content>div.modal-footer>div>div.pull-right>button.btn.btn-default")


class CreateProtocolPageLocators:
    BTN_CLOSE_TEMPLATE_SELECTION = (By.CSS_SELECTOR, "div.modal-header>button.close")
    PROTOCOL_FRAME = (By.CSS_SELECTOR, "iframe")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="description"]')
    CONCLUSION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="conclusion"]')
    RECOMMENDATION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="recommendation"]')
    BTN_EDITABLE = (By.CSS_SELECTOR, 'input#isEditableBottom')
    BTN_SAVE_PROTOCOL_AND_CONTINUE = (By.CSS_SELECTOR, 'div.flex1end div>button.btn.btn-default:not([id])')
    BTN_SAVE_PROTOCOL_AND_CLOSE = (By.CSS_SELECTOR, 'div.flex1end div>div.btn-group>button.btn.btn-primary:not([id])')
