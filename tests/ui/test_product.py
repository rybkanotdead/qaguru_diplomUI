import allure
from project_test_demoblaze.pages.main_page import MainPage
from project_test_demoblaze.pages.product_page import ProductPage
from project_test_demoblaze.pages.cart_page import CartPage
from allure_commons.types import Severity
from data.order_data import order


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.title("Добавление товара Samsung Galaxy S6 в корзину")
def test_add_product_to_cart():
    main_page = MainPage()
    product_page = ProductPage()

    main_page.open_main_page()
    main_page.open_product("Samsung galaxy s6")
    product_page.add_to_cart()
    main_page.open_cart()
    main_page.should_have_product_in_cart("Samsung galaxy s6")


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.title("Добавление товара в корзину и удаление с корзины")
def test_add_and_delete_product_from_cart():
    main_page = MainPage()
    product_page = ProductPage()
    cart_page = CartPage()

    main_page.open_main_page()
    main_page.open_product("Samsung galaxy s6")
    product_page.add_to_cart()

    cart_page.open_cart()
    main_page.should_have_product_in_cart("Samsung galaxy s6")

    cart_page.delete_product()
    cart_page.should_be_empty()


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.title("Добавление товара в корзину и оформление товара")
def test_add_product_and_place_order():
    main_page = MainPage()
    product_page = ProductPage()
    cart_page = CartPage()

    main_page.open_main_page()
    main_page.open_product("Samsung galaxy s6")
    product_page.add_to_cart()

    cart_page.open_cart()
    cart_page.place_order()
    cart_page.should_be_visible_order_modal()
    cart_page.fill_order_form(order)
    cart_page.submit_order()
    cart_page.should_see_success_alert()
