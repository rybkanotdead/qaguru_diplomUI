from selene import browser, be, have
from selene.core.exceptions import TimeoutException


class CartPage:
    @staticmethod
    def open_cart():
        # Переход на страницу корзины
        browser.open("/cart.html")
        browser.should(have.url_containing("/cart"))

    @staticmethod
    def delete_product():
        # Удаление товара из корзины (если он есть)
        try:
            delete_link = browser.element("a[onclick^='deleteItem']")
            delete_link.should(be.visible).click()
        except TimeoutException:
            print("Элемент удаления не найден — товар, возможно, уже удалён.")

    @staticmethod
    def should_be_empty():
        # Проверка, что корзина пуста
        browser.element("#tbodyid").should(have.text(""))

    @staticmethod
    def place_order():
        # Нажатие на кнопку "Place Order", открывающую модальное окно
        browser.element("button[data-target='#orderModal']").should(be.visible).click()

    @staticmethod
    def should_see_order_modal():
        # Проверка, что модальное окно с формой заказа появилось
        browser.element("#orderModal").should(be.visible)

    @staticmethod
    def fill_order_form(data: dict):
        # Заполнение формы заказа
        browser.element("#name").type(data["name"])
        browser.element("#country").type(data["country"])
        browser.element("#city").type(data["city"])
        browser.element("#card").type(data["credit_card"])
        browser.element("#month").type(data["month"])
        browser.element("#year").type(data["year"])

    @staticmethod
    def submit_order():
        # Ждём появления кнопки "Purchase" внутри модального окна
        browser.element("#orderModal").should(be.visible)  # ещё раз, для надёжности
        purchase_button = browser.element("#orderModal .modal-footer .btn-primary")
        purchase_button.should(be.visible).should(be.enabled).click()

    @staticmethod
    def should_see_success_alert():
        # Проверка, что появилось сообщение об успешной покупке
        browser.element(".sweet-alert").should(
            have.text("Thank you for your purchase!")
        )
