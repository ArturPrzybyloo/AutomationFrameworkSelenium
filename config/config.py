class ApplicationConfiguration:
    def __init__(self, base_url, user_name, password):
        self.base_url = base_url
        self.user_name = user_name
        self.password = password


class WebDriverConfiguration:
    def __init__(self, browser_name, default_timeout: int, headless: bool, full_screen: bool,
                 disable_notifications: bool):
        self.browser_name = browser_name
        self.default_timeout = default_timeout
        self.headless = headless
        self.full_screen = full_screen
        self.disable_notifications = disable_notifications


class Configuration:
    def __init__(self, application_configuration: ApplicationConfiguration,
                 web_driver_configuration: WebDriverConfiguration):
        self.application_configuration = application_configuration
        self.web_driver_configuration = web_driver_configuration
