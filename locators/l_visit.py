from selenium.webdriver.common.by import By


class VisitPageLocators:
    LABEL_FIO = (By.CSS_SELECTOR, 'div.menu-item-user>div.pull-right>div:nth-child(1)')
    STUDY_PAGE = (By.CSS_SELECTOR, 'div.pull-left>h1.pull-left')
    CREATE_VISIT = (By.CSS_SELECTOR, "a.btn.btn-primary[href='/visit/create/']")
    PATIENTS_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>a[href^='/share/visits/']")
    PATIENTS_BIRTHDAY_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>span:has(br)")
    PATIENTS_TYPES_OF_STUDY_LIST = (By.CSS_SELECTOR, 'ul.compact.style_marker_none>li>a[href^="/visit/"]')
    REFRESH_STUDY_PAGE = (By.CSS_SELECTOR, "i.fa.fa-refresh")


class CreateVisitPageLocators:
    # TABS
    TAB_BASE = (By.CSS_SELECTOR, "a#regform-tabs-tab-base")
    TAB_PARAMS = (By.CSS_SELECTOR, "a#regform-tabs-tab-params")
    TAB_ADDITIONAL = (By.CSS_SELECTOR, "a#regform-tabs-tab-additional")
    TAB_PASSPORT_REGISTRATION = (By.CSS_SELECTOR, "a#regform-tabs-tab-passport-registration")

    # MAIN
    DELETE_BUTTON = (By.CSS_SELECTOR, "div.clearfix>div.pull-left>button.btn.btn-danger")
    REASON_FOR_DELETE = (By.CSS_SELECTOR, "textarea#description")
    MODAL_ACTION_DELETE = (By.CSS_SELECTOR, "button#modal-action-delete")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>div.btn-toolbar[role='toolbar']>div>button.btn.btn-primary")
    LIST_SAVE_ACTIONS = (By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants")
    SELECT_ACTIONS = (
        By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants>div.react-select__menu>div>div")
    BLOCK_PAGE = (By.CSS_SELECTOR, "div[role='dialog']")

    class BaseTab:
        #   PERSON DATA
        EXTERNAL_ID = (By.CSS_SELECTOR, "input#external_id")
        POLIS_OMS = (By.CSS_SELECTOR,
                     "label.control-label[for='patient_polis_number']+div.btn-group.bootstrap-select.form-control.open>input.form-control[value]")
        SNILS = (By.CSS_SELECTOR,
                 "label.control-label[for='snils']+div.btn-group.bootstrap-select.form-control.open>input.form-control[value]")
        FULL_NAME = (By.CSS_SELECTOR, "input#full_name")
        BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
        SEX_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div")
        SEX = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div div[tabindex='-1']")
        SEX_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='sex']+div>div>div>div.react-select__single-value")
        PHONE_NUMBER = (By.CSS_SELECTOR, "input#phone_number")
        EMAIL = (By.CSS_SELECTOR, "input#email")
        ALLERGY_TYPE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='allergy_type']+div>div")
        ALLERGY_TYPE = (By.CSS_SELECTOR, "label.control-label[for='allergy_type']+div>div div[tabindex='-1']")
        ALLERGY_TYPE_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='allergy_type']+div>div>div>div.react-select__single-value")
        YEAR_DOSE = (By.CSS_SELECTOR, "input#year_dose[disabled]")
        #   DATA DIRECTION
        TREATMENT_CASE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='treatment_case']+div>div")
        TREATMENT_CASE = (By.CSS_SELECTOR, "label.control-label[for='treatment_case']+div>div div[tabindex='-1']")
        TREATMENT_CASE_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='treatment_case']+div>div>div>div.react-select__single-value")
        PATIENT_CLASS_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='patient_class']+div>div")
        PATIENT_CLASS = (By.CSS_SELECTOR, "label.control-label[for='patient_class']+div>div div[tabindex='-1']")
        PATIENT_CLASS_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='patient_class']+div>div>div>div.react-select__single-value")
        OUTPATIENT_CARD_NUMBER = (
            By.CSS_SELECTOR, "label.control-label[for='outpatient_card_number']+div>input.form-control")
        CASE_HISTORY_NUMBER = (By.CSS_SELECTOR, "label.control-label[for='case_history_number']+div>input.form-control")
        REF_DEPARTMENT = (By.CSS_SELECTOR, "label.control-label[for='ref_department']+div>input.form-control")
        REF_DOCTOR = (By.CSS_SELECTOR, "label.control-label[for='ref_doctor']+div>input.form-control")
        SOURCE_FINANCING_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='source_financing']+div>div")
        SOURCE_FINANCING = (By.CSS_SELECTOR, "label.control-label[for='source_financing']+div>div div[tabindex='-1']")
        SOURCE_FINANCING_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='source_financing']+div>div>div>div.react-select__single-value")
        PURPOSE = (By.CSS_SELECTOR, "label.control-label[for='purpose']+div>input.form-control")
        DIAGNOSES_MKB_CONTAINER = (By.CSS_SELECTOR, "div#diagnoses.jstree-widget")
        DIAGNOSES_MKB_SEARCH_INPUT = (By.CSS_SELECTOR, "div#diagnoses>div.jstree-widget-content>input")
        DIAGNOSES_MKB_NODES = (By.CSS_SELECTOR, "div#diagnoses>div.jstree-widget-content>div>ul>li.jstree-node")
        COMMENT = (By.CSS_SELECTOR, "textarea#comment")
        #   DATA STUDY
        DOCTOR_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='doctor']+div>div")
        ASSISTANT_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='assistant']+div>div")
        TYPES_OF_STUDY_CONTAINER = (
            By.CSS_SELECTOR, "label.control-label[for='studies']+div.studies-field>span div.react-select__control")
        TYPE_OF_STUDY = (By.CSS_SELECTOR, "label.control-label[for='studies']+div div[tabindex='-1']")
        DEVICE_CONTAINER = (By.CSS_SELECTOR,
                            'label[for="device"]+div>div>div.react-select__value-container.react-select__value-container--has-value')
        CONTRAST_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='contrast_enhancement']+div>div")
        CONTRAST_VOLUME = (By.CSS_SELECTOR, "input#contrast_volume")
        DOSE_RG = (By.CSS_SELECTOR, "input#doseRG")
        DOSE = (By.CSS_SELECTOR, "input#dose[disabled]")
        IS_CITO_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='is_cito']+div>div")
        IS_CITO = (By.CSS_SELECTOR, "label.control-label[for='is_cito']+div>div div[tabindex='-1']")
        IS_CITO_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='is_cito']+div>div>div>div.react-select__single-value")

    class ParamsTab:
        INSURANCE_COMPANY_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='insurance_company']+div>div")
        INSURANCE_COMPANY = (By.CSS_SELECTOR, "label.control-label[for='insurance_company']+div>div div[tabindex='-1']")
        INSURANCE_COMPANY_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='insurance_company']+div>div>div>div.react-select__single-value")
        INSURANCE_CONTRACT = (By.CSS_SELECTOR, "input#insurance_contract")
        POLIS_NUMBER = (By.CSS_SELECTOR, "input#polis_number")
        MEDICAL_DIAGNOSIS = (By.CSS_SELECTOR, "input#medical_diagnosis")
        ALTERNATE_ID = (By.CSS_SELECTOR, "input#alternate_id")
        HEIGHT = (By.CSS_SELECTOR, "input#height")
        WEIGHT = (By.CSS_SELECTOR, "input#weight")
        FILM_COUNT = (By.CSS_SELECTOR, "input#film_count")
        FLU_SIGN_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='fluSign']+div>div")
        FLU_SIGN_NO_DATE = (By.CSS_SELECTOR,
                            "label.control-label[for='fluSign']+div>div div.react-select__menu-notice.react-select__menu-notice--no-options")
        FLU_SIGN = (By.CSS_SELECTOR, "label.control-label[for='fluSign']+div>div div[tabindex='-1']")
        FLU_PURPOSE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='fluPurpose']+div>div")
        FLU_PURPOSE_NO_DATE = (By.CSS_SELECTOR,
                               "label.control-label[for='fluPurpose']+div>div div.react-select__menu-notice.react-select__menu-notice--no-options")
        FLU_PURPOSE = (By.CSS_SELECTOR, "label.control-label[for='fluPurpose']+div>div div[tabindex='-1']")
        REF_ID = (By.CSS_SELECTOR, "input#ref_id")
        REF_DATE = (By.CSS_SELECTOR, "input#ref_date")
        DIRECTION_TYPE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='direction_type']+div>div")
        DIRECTION_TYPE = (By.CSS_SELECTOR, "label.control-label[for='direction_type']+div>div div[tabindex='-1']")
        BENEFIT_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='benefit']+div>div")
        BENEFIT = (By.CSS_SELECTOR, "label.control-label[for='benefit']+div>div div[tabindex='-1']")
        FSIDIS_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='fsidis']+div>div")
        FSIDIS = (By.CSS_SELECTOR, "label.control-label[for='fsidis']+div>div div[tabindex='-1']")

    class AdditionalTab:
        CONSULTATION_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='customField23']+div>div")
        CONSULTATION = (By.CSS_SELECTOR, "label.control-label[for='customField23']+div>div div[tabindex='-1']")

    class PassportRegistrationTab:
        IDENTIFIER_TYPE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='identifier_type']+div>div")
        IDENTIFIER_TYPE = (By.CSS_SELECTOR, "label.control-label[for='identifier_type']+div>div div[tabindex='-1']")
        IDENTIFIER_TYPE_SELECT_VALUE = (
            By.CSS_SELECTOR, "label.control-label[for='identifier_type']+div>div>div>div.react-select__single-value")
        IDENTIFIER_SERIES = (By.CSS_SELECTOR, "input#identifier_series")
        IDENTIFIER_NUMBER = (By.CSS_SELECTOR, "input#identifier_number")
        IDENTIFIER_ISSUED = (By.CSS_SELECTOR, "input#identifier_issued")
        IDENTIFIER_DATE_ISSUED = (By.CSS_SELECTOR, "input#identifier_date_issued")
        REGISTRATION_STATE_NUMBER = (By.CSS_SELECTOR, "input#registration_state_number")
        REGISTRATION_SUBJECT = (By.CSS_SELECTOR, "input#registration_subject")
        REGISTRATION_REGISTRATION_DISTRICT = (
            By.CSS_SELECTOR, "label.control-label[for='registration_district']+div>input")
        REGISTRATION_CITY = (By.CSS_SELECTOR, "input#registration_city")
        REGISTRATION_LOCALITY = (By.CSS_SELECTOR, "input#registration_locality")
        REGISTRATION_STREET = (By.CSS_SELECTOR, "input#registration_street")
        REGISTRATION_HOUSE = (By.CSS_SELECTOR, "input#registration_house")
        REGISTRATION_APARTMENT = (By.CSS_SELECTOR, "input#registration_apartment")


class ComparisonVisitPageLocators:
    BUTTON_COMPARE = (By.CSS_SELECTOR,
                      "div.table-responsive>table.table.table-bordered.table-condensed>tbody>tr>td>button.btn.btn-default")


class CreateProtocolPageLocators:
    BUTTONS_CREATE_PROTOCOL = (By.CSS_SELECTOR, "a.no-underline[href$='/cd/CP/create']")
    BUTTON_CLOSE_TEMPLATE_SELECTION = (By.CSS_SELECTOR, "div.modal-header>button.close")
    PROTOCOL_FRAME = (By.CSS_SELECTOR, "iframe")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="description"]')
    CONCLUSION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="conclusion"]')
    RECOMMENDATION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="recommendation"]')
    BUTTON_EDITABLE = (By.CSS_SELECTOR, 'input#isEditableBottom')
    BUTTON_SAVE_PROTOCOL_AND_BACK = (By.CSS_SELECTOR, 'button.btn.btn-primary:not([id])')
