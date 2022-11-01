from pages.create_visit_page import CreateVisitPage


class TestCreateVisit:

    def test_create_visit(self, driver):
        page = CreateVisitPage(driver, 'https://nt.ris-x.com/')
        page.open()
        page.authorization()
        page.submit_and_fill_fields()
        assert 'https://nt.ris-x.com/' in page.current_url()
