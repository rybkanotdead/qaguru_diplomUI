import allure
from allure_commons.types import Severity
import config
from project_test_demoblaze import utils


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.tag("Authorization")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем статус-код при запросе токена")
def test_login_status_code():
    payload = {
        "username": config.settings.USER_LOGIN,
        "password": config.settings.API_PASSWORD,
    }
    with allure.step("Отправляем запрос"):
        response = utils.base_request.post("/login", json=payload)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.tag("Authorization")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем что вернулся токен")
def test_login_token():
    payload = {
        "username": config.settings.USER_LOGIN,
        "password": config.settings.API_PASSWORD,
    }
    with allure.step("Отправляем запрос"):
        response = utils.base_request.post("/login", json=payload)
        response_json = response.json()
        print("Response JSON:", response_json)  # для отладки

    with allure.step("Проверяем, что вернулся токен или ошибка"):
        if "errorMessage" in response_json:
            assert response_json["errorMessage"] == "Wrong password."
        else:
            assert "auth_token" in response_json or "token" in response_json
