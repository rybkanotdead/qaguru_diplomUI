import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
import logging

import config  # импорт твоего конфига с настройками из .env

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.demoblaze.com'

    if config.settings.ENVIRONMENT == 'local':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--headless')  # если нужно без UI
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

        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True,
            }
        }

        options.set_capability('selenoid:options', selenoid_capabilities['selenoid:options'])
        options.set_capability('browserName', selenoid_capabilities['browserName'])
        options.set_capability('browserVersion', selenoid_capabilities['browserVersion'])

        remote_url = f"https://{config.settings.SELENOID_LOGIN}:{config.settings.SELENOID_PASSWORD}@selenoid.autotests.cloud/wd/hub"
        logger.info(f"Remote Selenoid URL: {remote_url}")

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
        browser.config.driver = driver

    browser.config.timeout = 10

    yield
    browser.quit()
