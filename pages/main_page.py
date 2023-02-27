from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)

    # Locators
    # buttons
    register_button = (By.LINK_TEXT, "Register")
    register_submit_button = (By.XPATH, "//input[@type='submit']")
    register_form = (By.ID, "customerForm")
    # inputs
    first_name_input = (By.ID, "customer.firstName")
    last_name_input = (By.ID, "customer.lastName")
    address_input = (By.ID, "customer.address.street")
    city_input = (By.ID, "customer.address.city")
    state_input = (By.ID, "customer.address.state")
    zipcode_input = (By.ID, "customer.address.zipCode")
    phone_input = (By.ID, "customer.phoneNumber")
    ssn_input = (By.ID, "customer.ssn")
    username_input = (By.ID, "customer.username")
    password_input = (By.ID, "customer.password")
    repeat_password_input = (By.ID, "repeatedPassword")

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()
        self.driver.find_element(*self.register_button)

    def enter_first_name(self):
        self.driver.find_element(*self.first_name_input).send_keys("Monika")

    def enter_last_name(self):
        self.driver.find_element(*self.last_name_input).send_keys("Kowalska")

    def enter_address(self):
        self.driver.find_element(*self.address_input).send_keys("1060 Parkview Drive")

    def enter_city(self):
        self.driver.find_element(*self.city_input).send_keys("Houston")

    def enter_state(self):
        self.driver.find_element(*self.state_input).send_keys("Texas")

    def enter_zipcode(self):
        self.driver.find_element(*self.zipcode_input).send_keys("77074")

    def enter_phone_nr(self):
        self.driver.find_element(*self.phone_input).send_keys("713-981-3365")

    def enter_SSN(self):
        self.driver.find_element(*self.ssn_input).send_keys("713-981-3365")

    def enter_username(self):
        self.driver.find_element(*self.username_input).send_keys("monisia890")

    def enter_password(self):
        self.driver.find_element(*self.password_input).send_keys("koko890")

    def enter_repeated_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("koko890")












