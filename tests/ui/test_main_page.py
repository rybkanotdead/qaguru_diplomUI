import allure
from allure_commons.types import Severity
from project_test_demoblaze.pages.main_page import MainPage

main_page = MainPage()


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.title("Проверяем фильтрацию по телефонам")
def test_phones_filter():
    main_page.open_main_page()
    main_page.click_category("Phones")
    main_page.should_have_gadget("Samsung galaxy s6")


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.title("Проверяем фильтрацию по лэптопам")
def test_laptops_filter():
    main_page.open_main_page()
    main_page.click_category("Laptops")
    main_page.should_have_gadget("MacBook air")


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.title("Проверяем фильтрацию по мониторам")
def test_monitors_filter():
    main_page.open_main_page()
    main_page.click_category("Monitors")
    main_page.should_have_gadget("Apple monitor 24")
