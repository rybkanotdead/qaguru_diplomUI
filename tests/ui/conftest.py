import allure
import pytest
import requests
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from project_test_demoblaze.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.demoblaze.com'
    if config.settings.ENVIRONMENT == 'local':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        options = webdriver.ChromeOptions()
        browser.config.driver_options = options
    else:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(capabilities)

        login = config.settings.SELENOID_LOGIN
        password = config.settings.SELENOID_PASSWORD

        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
        browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if config.settings.ENVIRONMENT == 'remote':
        attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def api_token():
    payload = {
        'username': config.settings.USER_LOGIN,
        'password': config.settings.API_PASSWORD
    }
    with allure.step('Получаем токен авторизации'):
        response = requests.post(
            'https://api.demoblaze.com/login',
            json=payload
        )

    yield response.text.split()[1][:-1]