from selenium.webdriver.common.by import By


class VisitPageLocators:
    CREATE_VISIT = (By.CSS_SELECTOR, "a.btn.btn-primary[href='/visit/create/']")
    FULL_NAME = (By.CSS_SELECTOR, "input#full_name")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input#phone_number")
    EMAIL = (By.CSS_SELECTOR, "input#email")
    BIRTHDAY = (By.CSS_SELECTOR, "input#birth")
    SEX_CONTAINER = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div")
    SEX = (By.CSS_SELECTOR, "label.control-label[for='sex']+div>div div[tabindex='-1']")
    TYPES_OF_STUDY_CONTAINER = (
        By.CSS_SELECTOR, "label.control-label[for='studies']+div.studies-field>span div.react-select__control")
    TYPE_OF_STUDY = (By.CSS_SELECTOR, "label.control-label[for='studies']+div div[tabindex='-1']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>div.btn-toolbar[role='toolbar']>div>button.btn.btn-primary")
    LIST_SAVE_ACTIONS = (By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants")
    SELECT_ACTIONS = (By.CSS_SELECTOR, "div.btn-toolbar[role='toolbar']>div>div.save-actions-variants>div.react-select__menu>div>div")
    PATIENTS_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>a[href^='/share/visits/']")
    PATIENTS_BIRTHDAY_LIST = (By.CSS_SELECTOR, "div.table-responsive>table>tbody>tr>td>span:has(br)")
    PATIENTS_TYPES_OF_STUDY_LIST = (By.CSS_SELECTOR, 'ul.compact.style_marker_none>li>a[href^="/visit/"]')
    REFRESH_STUDY_PAGE = (By.CSS_SELECTOR, "i.fa.fa-refresh")


class CreateProtocolLocators:
    BUTTONS_CREATE_PROTOCOL = (By.CSS_SELECTOR, "a.no-underline[href$='/cd/CP/create']")
    BUTTON_CLOSE_TEMPLATE_SELECTION = (By.CSS_SELECTOR, "div.modal-header>button.close")
    PROTOCOL_FRAME = (By.CSS_SELECTOR, "iframe")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="description"]')
    CONCLUSION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="conclusion"]')
    RECOMMENDATION_FIELD = (By.CSS_SELECTOR, 'body#tinymce>div[data-tpl-block-id="recommendation"]')
    BUTTON_EDITABLE = (By.CSS_SELECTOR, 'input#isEditableBottom')
    BUTTON_SAVE_PROTOCOL_AND_BACK = (By.CSS_SELECTOR, 'button.btn.btn-primary:not([id])')
