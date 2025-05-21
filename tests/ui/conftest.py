import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser
from dotenv import load_dotenv

load_dotenv()

# Простейшая замена pydantic_settings
class Settings:
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
    USER_LOGIN = os.getenv('USER_LOGIN')
    USER_PASSWORD = os.getenv('USER_PASSWORD')
    API_PASSWORD = os.getenv('API_PASSWORD')
    SELENOID_LOGIN = os.getenv('SELENOID_LOGIN')
    SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD')

settings = Settings()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.demoblaze.com'

    if settings.ENVIRONMENT == 'local':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--headless')  # для запуска без UI
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        browser.config.driver = driver

    elif settings.ENVIRONMENT == 'remote':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        options.set_capability("selenoid:options", selenoid_capabilities["selenoid:options"])
        options.set_capability("browserName", selenoid_capabilities["browserName"])
        options.set_capability("browserVersion", selenoid_capabilities["browserVersion"])

        remote_url = f"https://{settings.SELENOID_LOGIN}:{settings.SELENOID_PASSWORD}@selenoid.autotests.cloud/wd/hub"
        driver = webdriver.Remote(command_executor=remote_url, options=options)
        browser.config.driver = driver

    yield

    browser.quit()