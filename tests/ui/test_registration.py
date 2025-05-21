import allure
from selene import browser, be, have
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project_test_demoblaze.pages.main_page import MainPage
from project_test_demoblaze.pages.sign_up_page import SignUpPage
from data.user_data import generate_user_data
from allure_commons.types import Severity


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.title("Регистрация нового пользователя")
def test_user_registration():
    user_data = generate_user_data()
    main_page = MainPage()
    sign_up_page = SignUpPage()

    with allure.step("Открываем главную страницу и модалку регистрации"):
        main_page.open_main_page()

        sign_in_button = browser.driver.find_element(By.ID, "signin2")

        # Скроллим к кнопке и кликаем по ней, когда она будет кликабельной
        ActionChains(browser.driver).move_to_element(sign_in_button).perform()
        WebDriverWait(browser.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin2"))
        )
        sign_in_button.click()

        # Убеждаемся, что модальное окно появилось
        browser.element('#sign-username').should(be.visible)

    with allure.step("Заполняем форму регистрации"):
        browser.element('#sign-username').type(user_data["username"])
        browser.element('#sign-password').type(user_data["password"])

    with allure.step("Подтверждаем регистрацию"):
        sign_up_page.submit_registration()

    with allure.step("Проверка успешной регистрации через alert"):
        try:
            WebDriverWait(browser.driver, 5).until(EC.alert_is_present())
            alert = browser.driver.switch_to.alert
            assert "Sign up successful" in alert.text
            alert.accept()
        except Exception:
            # В редких случаях alert может не появиться — fallback на сообщение на странице
            browser.element('.alert-success').should(have.text("Sign up successful"))
