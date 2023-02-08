import pytest

from config.config_provider import ConfigProvider
from webdriver.web_driver_factory import WebDriverFactory


@pytest.fixture()
def driver(request):
    config = ConfigProvider()
    wd = WebDriverFactory(config.configuration).create_driver()
    session = request.node
    cls = session.getparent(pytest.Class)
    setattr(cls.obj, "driver", wd)
    request.addfinalizer(wd.quit)
    return wd
