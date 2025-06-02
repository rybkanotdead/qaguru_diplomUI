import allure
import jsonschema
import pytest
from allure_commons.types import Severity
from project_test_demoblaze.api.base_request import base_request
from project_test_demoblaze.api.load_json_schema import load_schema


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем статус-код и содержимое при выборе категории")
@pytest.mark.parametrize("cat", ["monitor", "laptops", "phones"])
def test_categories(cat):
    payload = {"cat": cat}
    with allure.step("Отправляем запрос"):
        response = base_request.post("/bycat", json=payload)

    with allure.step("Проверяем статус-код и содержимое"):
        assert response.status_code == 200
        body = response.json()
        for item in body["Items"]:
            assert item["cat"] == cat


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.title("Валидируем JSON-схему при выборе категории")
@pytest.mark.parametrize("cat", ["monitor", "laptops", "phones"])
def test_categories_validate_json_schema(cat):
    payload = {"cat": cat}
    with allure.step("Отправляем запрос"):
        response = base_request.post("/bycat", json=payload)

    with allure.step("Валидируем JSON-схему"):
        jsonschema.validate(response.json(), load_schema("list_json_schema.json"))
