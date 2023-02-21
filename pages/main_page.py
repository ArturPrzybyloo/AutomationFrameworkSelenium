from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

        # Locators
        register_button = (By.LINK_TEXT, "Register")
        register_form = (By.ID, "customerForm")
        first_name_input =  (By.ID, "customer.firstName")
        last_name_input =  (By.ID, "customer.lastName")
        address_input = (By.ID, "customer.address.street")

        # Methods
        def click_register_button(self):
            self.driver.find_element(*self.register_button).click()
            self.driver.find_element(*self.register_button)


        def enter_first_name(self, first_name):
            self.driver.find_element(*self.first_name_input).send_keys(first_name)

