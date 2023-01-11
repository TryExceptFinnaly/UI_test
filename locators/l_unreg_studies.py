from selenium.webdriver.common.by import By


class UnregStudiesPageLocators:
    @staticmethod
    def get_unreg_studies_locator(name: str, birthdate: str, sex: str, id: str = '', study: str = '', part: str = '',
                                  mo: str = '', room: str = '', device: str = '', modality: str = ''):
        locator = "//tr[td[2]]"
        # Required
        prefix_name = f"[td[5][span[text()='{name}']][div[text()='{name}']]]"
        prefix_birthdate = f"[td[6][text()='{birthdate}']]"
        prefix_sex = f"[td[7][text()='{sex}']]"
        # Optional
        prefix_id = f"[td[4][text()='{id}']]" if id else ''
        prefix_study = f"[td[8][span[text()='{study}']]]" if study else ''
        prefix_part = f"[td[9][text()='{part}']]" if part else ''
        prefix_mo = f"[td[10][span[text()='{mo}']]]" if mo else ''
        prefix_room = f"[td[11][span[text()='{room}']]]" if room else ''
        prefix_device = f"[td[12][span[text()='{device}']]]" if device else ''
        prefix_modality = f"[td[13][text()='{modality}']]" if modality else ''
        locator += prefix_name + prefix_birthdate + prefix_sex + prefix_id + prefix_study + prefix_part + prefix_mo + prefix_room + prefix_device + prefix_modality
        return By.XPATH, locator
    BTN_DELETE = (By.XPATH, "//td[1]/a/i[@class='fa fa-trash']")
    BTN_MODAL_DELETE_YES = (
        By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer>button.btn.btn-danger")
    BTN_MODAL_DELETE_NO = (
        By.CSS_SELECTOR, "div[role='dialog']>div>div.modal-content>div.modal-footer>button.btn.btn-default")
    REFRESH_PAGE = (By.XPATH, "//div[@class='form-group']/a/i[@class='fa fa-refresh']")
