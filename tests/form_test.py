from time import sleep
from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://nt.ris-x.com/')
        form_page.open()
        form_page.fill_fields_and_submit()
        user_name, study_page, planned_page = form_page.check_data_page()
        sleep(5)
        assert user_name == 'Дубровин А. В.'
        assert study_page == 'Исследования'
        assert planned_page == 'Запланированные'
