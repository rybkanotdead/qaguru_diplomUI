import os
import shutil
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import get_cache_dir  # для очистки кэша

from selene.support.shared import browser

from config import settings


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    load_dotenv()
    browser.config.base_url = 'https://www.demoblaze.com'
    browser.config.timeout = 10

    if settings.ENVIRONMENT == 'remote':
        print('[INFO] Using remote driver (Selenoid)')
        options = Options()
        options.add_argument('--window-size=1920,1080')

        capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        login = os.getenv("SELENOID_LOGIN", "user1")
        password = os.getenv("SELENOID_PASSWORD", "1234")
        remote_url = f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub"

        browser.config.driver = webdriver.Remote(
            command_executor=remote_url,
            options=options,
            desired_capabilities=capabilities
        )
    else:
        print('[INFO] Using local driver')
        options = Options()
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--headless')  # раскомментируй если нужно без GUI
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        try:
            # вручную удаляем кэш драйвера, если нужно (опционально)
            cache_dir = get_cache_dir()
            shutil.rmtree(cache_dir, ignore_errors=True)
            print(f'[INFO] Cache directory {cache_dir} deleted')
        except Exception as e:
            print(f'[WARNING] Could not delete cache: {e}')

        driver_path = ChromeDriverManager().install()
        print(f'[INFO] Using ChromeDriver from: {driver_path}')

        service = Service(driver_path)
        browser.config.driver = webdriver.Chrome(service=service, options=options)

    yield
    browser.quit()
