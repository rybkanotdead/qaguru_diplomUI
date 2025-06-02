import allure
from selene import browser, be


class ProductPage:

    @allure.step("Нажимаем кнопку Add to cart")
    def add_to_cart(self):
        browser.element("a.btn.btn-success").should(be.visible).click()
