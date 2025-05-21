import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser
from your_project import config  # замените на ваш путь импорта config

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.demoblaze.com'

    if config.settings.ENVIRONMENT == 'local':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--headless')  # если нужен без UI
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        browser.config.driver = driver

    else:  # remote (Selenoid)
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-notifications')

        selenoid_caps = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        for key, value in selenoid_caps.items():
            options.set_capability(key, value)

        remote_url = f"http://{config.settings.SELENOID_LOGIN}:{config.settings.SELENOID_PASSWORD}@selenoid.autotests.cloud/wd/hub"
        logger.info(f"Remote Selenoid URL: {remote_url}")

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
        browser.config.driver = driver

    yield
    browser.quit()
