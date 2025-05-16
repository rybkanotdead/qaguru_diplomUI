import allure
from selene import browser

import config


class LoginForm:
    @allure.step('Заполняем данные пользователя')
    def fill_user(self):
        browser.element('#loginusername').type(config.settings.USER_LOGIN)
        browser.element('#loginpassword').type(config.settings.USER_PASSWORD)

    @allure.step('Нажимаем кнопку "Log In"')
    def click_login(self):
        browser.element('[onclick="logIn()"]').click()