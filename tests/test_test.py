from pages.main_page import MainPage


class TestSearch:
    def test_search_multiple_results(self, driver):
        """ Tests search for specific word and verify results"""
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        mp = MainPage(driver)
        mp.click_register_button()
        print(driver.title)