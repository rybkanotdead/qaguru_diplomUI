import allure
from selene import be, browser, have
from selene.core import query


class MainPage:
    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        browser.open("/")

    @allure.step("Открываем окно авторизации")
    def open_login_window(self):
        browser.element("#login2").with_(click_by_js=True).click()

    @staticmethod
    def click_category(category_name: str):
        with allure.step(f"Кликаем на кнопку {category_name}"):
            browser.all(".list-group>a").element_by(have.text(category_name)).click()

    @staticmethod
    @allure.step("Проверяем регистрацию пользователя")
    def should_have_registered(username):
        user_element = (
            browser.element("#nameofuser").should(be.present).with_(timeout=10)
        )
        actual_text = user_element.get(query.text)
        print(f'DEBUG: Ожидаем "Welcome {username}", а на странице: "{actual_text}"')
        user_element.should(have.exact_text(f"Welcome {username}"))

    @staticmethod
    @allure.step('Проверяем что "{value}" есть в списке')
    def should_have_gadget(value):
        browser.element("#tbodyid").should(have.text(value))

    @staticmethod
    @allure.step('Открываем страницу товара "{product_name}"')
    def open_product(product_name: str):
        browser.element("a.hrefch").should(have.exact_text(product_name)).click()

    @staticmethod
    @allure.step("Открываем корзину")
    def open_cart():
        browser.all("a.nav-link").element_by(have.text("Cart")).click()

    @staticmethod
    def should_have_product_in_cart(product_name):
        browser.all("tr.success").element_by(have.text(product_name)).should(be.visible)

    @staticmethod
    @allure.step("Открываем окно регистрации")
    def open_sign_up_window():
        browser.element("#signin2").should(be.visible).click()
