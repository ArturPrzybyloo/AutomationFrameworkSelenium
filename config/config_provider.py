import json

from config.config import Configuration, ApplicationConfiguration, WebDriverConfiguration


class ConfigProvider:
    def __init__(self):
        self.configuration = self.load_config()



    def load_config(self):
        with open("C:/Users/HP/PycharmProjects/AutomationFrameworkSelenium/config/config.json", "r") as config:
            config_json = json.loads(config.read())
            webdriver_config = WebDriverConfiguration(**config_json['web_driver_configuration'])
            app_configuration = ApplicationConfiguration(**config_json['application_configuration'])
            configuration = Configuration(application_configuration=app_configuration,
                                          web_driver_configuration=webdriver_config)
            return configuration
