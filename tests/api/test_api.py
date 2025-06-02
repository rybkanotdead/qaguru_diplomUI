import allure
import jsonschema
import pytest
from allure_commons.types import Severity

from project_test_demoblaze import utils


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем статус-код при выборе категории")
@pytest.mark.parametrize("cat", ["monitor", "laptops", "phones"])
def test_categories_status_code(cat):
    payload = {"cat": cat}
    with allure.step("Отправляем запрос"):
        response = utils.base_request.post("/bycat", json=payload)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200


@allure.label("owner", "alina oga")
@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем фильтрацию при выборе категории")
@pytest.mark.parametrize("cat", ["monitor", "laptops", "phones"])
def test_categories_items(cat):
    payload = {"cat": cat}
    with allure.step("Отправляем запрос"):
        response = utils.base_request.post("/bycat", json=payload)

    body = response.json()
    with allure.step(f"Проверяем, что вернулась категория {cat}"):
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
        response = utils.base_request.post("/bycat", json=payload)

    with allure.step("Валидируем JSON-схему"):
        jsonschema.validate(response.json(), utils.load_schema("list_json_schema.json"))
