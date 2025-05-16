import allure
from allure_commons.types import Severity

from project_test_demoblaze.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем лейбл в шапке сайта')
def test_label():
    main_page.open_main_page()

    main_page.should_label_be_clickable_and_have_text()


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем панель навигации')
def test_header():
    main_page.open_main_page()

    main_page.should_be_navbar_example()


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем заголовок блока CATEGORIES')
def test_categories():
    main_page.open_main_page()

    main_page.should_categories_be_clickable()


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по телефонам')
def test_phones_filter():
    main_page.open_main_page()

    main_page.click_phones()

    main_page.should_have_gadget('Samsung galaxy s6')


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по лэптопам')
def test_laptops_filter():
    main_page.open_main_page()

    main_page.click_laptops()

    main_page.should_have_gadget('MacBook air')


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по мониторам')
def test_monitors_filter():
    main_page.open_main_page()

    main_page.click_monitors()

    main_page.should_have_gadget('Apple monitor 24')


@allure.label('owner', 'alina oga')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем подвал сайта')
def test_footer():
    main_page.open_main_page()

    main_page.should_footer_have_text()