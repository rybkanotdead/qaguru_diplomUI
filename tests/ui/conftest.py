import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
import config
import logging
from project_test_demoblaze.utils import attach

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://www.demoblaze.com"

    if config.settings.ENVIRONMENT == "local":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        browser.config.driver = driver

    else:  # remote (Selenoid)
        options = Options()
        caps = {
            "browserName": "chrome",
            "browserVersion": "127.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            },
        }
        remote_url = (
            f"https://{config.settings.SELENOID_LOGIN}:"
            f"{config.settings.SELENOID_PASSWORD}"
            "@selenoid.autotests.cloud/wd/hub"
        )
        logger.info(f"Remote Selenoid URL: {remote_url}")

        options.capabilities.update(caps)
        driver = webdriver.Remote(
            command_executor=(
                f"https://{config.settings.SELENOID_LOGIN}:"
                f"{config.settings.SELENOID_PASSWORD}"
                "@selenoid.autotests.cloud/wd/hub"
            ),
            options=options,
        )
        browser.config.driver = driver

    browser.config.timeout = 10

    yield
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)
    browser.quit()
