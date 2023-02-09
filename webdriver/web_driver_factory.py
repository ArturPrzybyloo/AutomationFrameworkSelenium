"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from config.config import Configuration
from config.config_provider import ConfigProvider


class WebDriverFactory:
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def create_driver(self):
        """
       Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        if self.configuration.web_driver_configuration.browser_name == "Ie":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.configuration.web_driver_configuration.browser_name == "Firefox":
            # Set ff driver
            driver = webdriver.Firefox()
        elif self.configuration.web_driver_configuration.browser_name == "Chrome":
            # Set chrome driver
            chrome_options, d = self._prepare_chrome_options()
            driver = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
        else:
            raise Exception(f"Browser: {self.configuration.web_driver_configuration.browser_name} not implemented!!")
        return driver

    def _prepare_chrome_options(self):
        browser_options = webdriver.ChromeOptions()
        if self.configuration.web_driver_configuration.headless:
            browser_options.add_argument("--headless")
            browser_options.add_argument('--no-sandbox')
            browser_options.add_argument('--window-size=1920,1200')
            browser_options.add_argument('--disable-gpu')
            browser_options.add_argument('--disable-dev-shm-usage')
        if self.configuration.web_driver_configuration.full_screen:
            browser_options.add_argument("--start-fullscreen")
        if self.configuration.web_driver_configuration.disable_notifications:
            browser_options.add_argument("--disable-notifications")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'WARNING'}
        d['perfLoggingPrefs'] = {'enableNetwork': 'true'}
        d['goog:loggingPrefs'] = {'performance': 'ALL'}
        return browser_options, d
