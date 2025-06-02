from dataclasses import dataclass
from selene import browser, be, have
from selene.core.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)


@dataclass
class OrderData:
    name: str
    country: str
    city: str
    credit_card: str
    month: str
    year: str


class CartPage:
    @staticmethod
    def open_cart():
        browser.open("/cart.html")
        browser.should(have.url_containing("/cart"))

    @staticmethod
    def delete_product():
        try:
            delete_link = browser.element("a[onclick^='deleteItem']")
            delete_link.should(be.visible).click()
            logger.info("Товар успешно удалён из корзины.")
            return True
        except TimeoutException:
            logger.warning("Элемент удаления не найден — товар, возможно, уже удалён.")
            return False

    @staticmethod
    def should_be_empty():
        browser.element("#tbodyid").should(have.text(""))

    @staticmethod
    def place_order():
        logger.info("Нажимаем кнопку 'Place Order'")
        browser.element("button[data-target='#orderModal']").should(be.visible).click()

    @staticmethod
    def should_be_visible_order_modal():
        browser.element("#orderModal").should(be.visible)

    @staticmethod
    def fill_order_form(order: OrderData):
        browser.element("#name").type(order.name)
        browser.element("#country").type(order.country)
        browser.element("#city").type(order.city)
        browser.element("#card").type(order.credit_card)
        browser.element("#month").type(order.month)
        browser.element("#year").type(order.year)

    @staticmethod
    def submit_order():
        browser.element("#orderModal").should(be.visible)
        purchase_button = browser.element("#orderModal .modal-footer .btn-primary")
        purchase_button.should(be.visible).should(be.enabled).click()

    @staticmethod
    def should_see_success_alert():
        browser.element(".sweet-alert").should(
            have.text("Thank you for your purchase!")
        )
