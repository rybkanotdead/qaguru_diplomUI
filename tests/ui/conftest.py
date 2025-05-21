import allure
import pytest
from selene import browser
from selenium import webdriver
from config import settings  # импортируй свой конфиг
from helpers.web import ui_attach

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    env = settings.ENVIRONMENT.lower()
    browser_version = settings.BROWSER_VERSION  # например, 'latest'
    window_width, window_height = settings.WINDOW_SIZE.split('x')
    timeout = settings.WEB_TIMEOUT  # например, 10

    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    )

    browser.config.driver_options = options
    browser.config.base_url = 'https://stepik.org'  # поменяй, если нужно
    browser.config.window_width = int(window_width)
    browser.config.window_height = int(window_height)
    browser.config.timeout = timeout

    if env == 'remote':
        with allure.step(f"Инициализация удалённого браузера Chrome {browser_version} через Selenoid"):
            selenoid_caps = {
                "browserName": "chrome",
                "browserVersion": browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_caps)
            remote_url = (
                f"https://{settings.SELENOID_LOGIN}:{settings.SELENOID_PASSWORD}"
                f"@{settings.SELENOID_URL}/wd/hub"
            )
            browser.config.driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )
    else:
        with allure.step("Инициализация локального браузера Chrome"):
            browser.config.driver = webdriver.Chrome(options=options)

    yield browser

    ui_attach.add_screenshot(browser)
    ui_attach.add_html(browser)
    ui_attach.add_logs(browser)
    if env == 'remote':
        ui_attach.add_video_from_selenoid(browser)

    browser.quit()
