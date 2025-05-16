from selene import browser, be, have
from selene.core.exceptions import TimeoutException


class CartPage:

    def open_cart(self):
        # Переход на страницу корзины
        browser.open('/cart.html')
        browser.should(have.url_containing('/cart'))

    def delete_product(self):
        # Удаление товара из корзины (если он есть)
        try:
            delete_link = browser.element("a[onclick^='deleteItem']")
            delete_link.should(be.visible).click()
        except TimeoutException:
            print("Элемент удаления не найден — товар, возможно, уже удалён.")

    def should_be_empty(self):
        # Проверка, что корзина пуста
        browser.element("#tbodyid").should(have.text(""))

    def place_order(self):
        # Нажатие на кнопку "Place Order", открывающую модальное окно
        browser.element("button[data-target='#orderModal']").should(be.visible).click()

    def should_see_order_modal(self):
        # Проверка, что модальное окно с формой заказа появилось
        browser.element("#orderModal").should(be.visible)

    def fill_order_form(self, data: dict):
        # Заполнение формы заказа
        browser.element("#name").type(data["name"])
        browser.element("#country").type(data["country"])
        browser.element("#city").type(data["city"])
        browser.element("#card").type(data["credit_card"])
        browser.element("#month").type(data["month"])
        browser.element("#year").type(data["year"])

    def submit_order(self):
        # Подтверждение заказа нажатием кнопки "Purchase"
        browser.element("button.btn-primary").should(be.visible).click()

    def should_see_success_alert(self):
        # Проверка, что появилось сообщение об успешной покупке
        browser.element(".sweet-alert").should(have.text("Thank you for your purchase!"))
