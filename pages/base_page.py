from pypom import Page
from faker import Faker
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config.config_provider import ConfigProvider


class BasePage(Page):

    def __init__(self, driver, **url):
        super().__init__(driver, **url)
        self.config = ConfigProvider().configuration
        self.wait = WebDriverWait(driver, self.config.web_driver_configuration.default_timeout)
        self.ec = ec
        self.fake = Faker()
