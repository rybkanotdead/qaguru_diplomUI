import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
import logging

import config

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
        caps = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        remote_url = f"http://{config.settings.SELENOID_LOGIN}:{config.settings.SELENOID_PASSWORD}@selenoid.autotests.cloud/wd/hub"
        logger.info(f"Remote Selenoid URL: {remote_url}")

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=Options(),  # пустые опции, если не нужно добавлять что-то конкретное
            desired_capabilities=caps  # Важно: для backward compatibility
        )
        browser.config.driver = driver

    browser.config.timeout = 10

    yield

    browser.quit()
