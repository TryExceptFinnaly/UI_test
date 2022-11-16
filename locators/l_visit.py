from selenium.webdriver.common.by import By


class VisitPageLocators:
    LABEL_FIO = (By.CSS_SELECTOR, 'div.menu-item-user>div.pull-right>div:nth-child(1)')
    STUDY_PAGE = (By.CSS_SELECTOR, 'div.pull-left>h1.pull-left')
    CREATE_VISIT = (By.CSS_SELECTOR, "a.btn.btn-primary[href='/visit/create/']")
    PATIENTS_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>a[href^='/share/visits/']")
    PATIENTS_BIRTHDAY_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>span:has(br)")
    PATIENTS_TYPES_OF_STUDY_LIST = (By.CSS_SELECTOR, 'ul.compact.style_marker_none>li>a[href^="/visit/"]')
    REFRESH_STUDY_PAGE = (By.CSS_SELECTOR, "i.fa.fa-refresh")
    PAGE_NOTIFICATIONS = (By.CSS_SELECTOR, 'div.notification.notification-success>div.notification-message>div.message')


class CreateVisitPageLocators:
    #   PERSON DATA
    EXTERNAL_ID = (By.CSS_SELECTOR, "input#external_id")
    POLIS_OMS = (By.CSS_SELECTOR, "label.control-label[for='patient_polis_number']+div>input.form-control")
    SNILS = (By.CSS_SELECTOR, "label.control-label[for='snils']+div>input.form-control")
    FULL_NAME = (By.CSS_SELECTOR, "input#full_name")
    BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
    SEX_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div")
    SEX = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div div[tabindex='-1']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input#phone_number")
    EMAIL = (By.CSS_SELECTOR, "input#email")
    ALLERGY_TYPE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='allergy_type']+div>div")
    ALLERGY_TYPE = (By.CSS_SELECTOR, "label.control-label[for='allergy_type']+div>div div[tabindex='-1']")
    YEAR_DOSE = (By.CSS_SELECTOR, "input#year_dose[disabled]")
    #   DATA DIRECTION
    TREATMENT_CASE_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='treatment_case']+div>div")
    TREATMENT_CASE = (By.CSS_SELECTOR, "label.control-label[for='treatment_case']+div>div div[tabindex='-1']")
    PATIENT_CLASS_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='patient_class']+div>div")
    PATIENT_CLASS = (By.CSS_SELECTOR, "label.control-label[for='patient_class']+div>div div[tabindex='-1']")
    OUTPATIENT_CARD_NUMBER = (
        By.CSS_SELECTOR, "label.control-label[for='outpatient_card_number']+div>input.form-control")
    CASE_HISTORY_NUMBER = (By.CSS_SELECTOR, "label.control-label[for='case_history_number']+div>input.form-control")
    REF_DEPARTMENT = (By.CSS_SELECTOR, "label.control-label[for='ref_department']+div>input.form-control")
    REF_DOCTOR = (By.CSS_SELECTOR, "label.control-label[for='ref_doctor']+div>input.form-control")
    SOURCE_FINANCING_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='source_financing']+div>div")
    SOURCE_FINANCING = (By.CSS_SELECTOR, "label.control-label[for='source_financing']+div>div div[tabindex='-1']")
    PURPOSE = (By.CSS_SELECTOR, "label.control-label[for='purpose']+div>input.form-control")
    DIAGNOSES_MKB_CONTAINER = (By.CSS_SELECTOR, "div#diagnoses")
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
    # MAIN
    DELETE_BUTTON = (By.CSS_SELECTOR, "div.clearfix>div.pull-left>button.btn.btn-danger")
    REASON_FOR_DELETE = (By.CSS_SELECTOR, "textarea#description")
    MODAL_ACTION_DELETE = (By.CSS_SELECTOR, "button#modal-action-delete")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>div.btn-toolbar[role='toolbar']>div>button.btn.btn-primary")
    LIST_SAVE_ACTIONS = (By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants")
    SELECT_ACTIONS = (
        By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants>div.react-select__menu>div>div")
    BLOCK_PAGE = (By.CSS_SELECTOR, "div[role='dialog']")


class CreateProtocolPageLocators:
    BUTTONS_CREATE_PROTOCOL = (By.CSS_SELECTOR, "a.no-underline[href$='/cd/CP/create']")
    BUTTON_CLOSE_TEMPLATE_SELECTION = (By.CSS_SELECTOR, "div.modal-header>button.close")
    PROTOCOL_FRAME = (By.CSS_SELECTOR, "iframe")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="description"]')
    CONCLUSION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="conclusion"]')
    RECOMMENDATION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="recommendation"]')
    BUTTON_EDITABLE = (By.CSS_SELECTOR, 'input#isEditableBottom')
    BUTTON_SAVE_PROTOCOL_AND_BACK = (By.CSS_SELECTOR, 'button.btn.btn-primary:not([id])')
