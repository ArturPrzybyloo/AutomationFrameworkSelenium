from pages.main_page import MainPage


class TestSearch:
    def test_search_multiple_results(self, driver):
        """ Tests search for specific word and verify results"""
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        mp = MainPage(driver)
        mp.click_register_button()
        mp.enter_first_name()
        mp.enter_last_name()
        mp.enter_address()
        mp.enter_city()
        mp.enter_state()
        mp.enter_zipcode()
        mp.enter_phone_nr()
        mp.enter_SSN()
        mp.enter_username()
        mp.enter_password()
        mp.enter_repeated_password()
        print(driver.title)