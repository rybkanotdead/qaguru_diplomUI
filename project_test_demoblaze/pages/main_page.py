import time

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

    @allure.step("Кликаем на кнопку Phones")
    def click_phones(self):
        browser.all(".list-group>a").element_by(have.text("Phone")).click()

    @allure.step("Кликаем на кнопку Laptops")
    def click_laptops(self):
        browser.all(".list-group>a").element_by(have.text("Laptops")).click()

    @allure.step("Кликаем на кнопку Monitors")
    def click_monitors(self):
        browser.all(".list-group>a").element_by(have.text("Monitors")).click()

    @staticmethod
    def token_to_cookie(api_token):
        api_token_encoded = browser.execute_script(
            "return encodeURIComponent(arguments[0]);", api_token
        )
        browser.execute_script(
            f'document.cookie = "auth_token={api_token_encoded}; path=/"'
        )

        # ⏳ Подождём чуть-чуть перед перезагрузкой страницы
        time.sleep(1)

        browser.open(browser.driver.current_url)

    @staticmethod
    @allure.step("Проверяем регистрацию пользователя")
    def should_have_registered(username):
        # Явное ожидание появления элемента
        user_element = (
            browser.element("#nameofuser").should(be.present).with_(timeout=10)
        )

        # Отладочный вывод
        actual_text = user_element.get(query.text)
        print(f'DEBUG: Ожидаем "Welcome {username}", а на странице: "{actual_text}"')

        # Проверка
        user_element.should(have.exact_text(f"Welcome {username}"))

    @staticmethod
    @allure.step("Проверяем лейбл")
    def should_label_be_clickable_and_have_text():
        browser.element("nav #nava").should(be.clickable)
        browser.element("nav #nava").should(have.text("PRODUCT STORE"))

    @staticmethod
    @allure.step("Проверяем панель навигации")
    def should_be_navbar_example():
        browser.all("[id=navbarExample] li").should(
            have.exact_texts(
                "Home\n(current)",
                "Contact",
                "About us",
                "Cart",
                "Log in",
                "",
                "",
                "Sign up",
            )
        )

    @staticmethod
    @allure.step("Проверяем надпись CATEGORIES")
    def should_categories_be_clickable():
        browser.element(".list-group #cat").should(have.exact_text("CATEGORIES"))
        browser.element(".list-group #cat").should(be.clickable)

    @staticmethod
    @allure.step('Проверяем что "{value}" есть в списке')
    def should_have_gadget(value):
        browser.element("#tbodyid").should(have.text(value))

    @staticmethod
    @allure.step("Проверяем подвал сайта")
    def should_footer_have_text():
        browser.all("div#footc h4").should(
            have.exact_texts("About Us", "Get in Touch", "PRODUCT STORE")
        )
        browser.all("div#footc p").should(
            have.exact_texts(
                (
                    "We believe performance needs to be validated"
                    " at every stage of the software development cycle"
                    " and our open source compatible, massively scalable"
                    " platform makes that a reality."
                ),
                "Address: 2390 El Camino Real",
                "Phone: +440 123456",
                "Email: demo@blazemeter.com",
            )
        )

    @staticmethod
    @allure.step("Открываем страницу товара Samsung galaxy s6")
    def open_product_s6():
        browser.element("a.hrefch") \
            .should(be.visible) \
            .should(have.exact_text("Samsung galaxy s6")) \
            .click()

    @staticmethod
    @allure.step("Открываем корзину")
    def open_cart():
        browser.all("a.nav-link").element_by(have.text("Cart")).click()

    @staticmethod
    def should_have_product_in_cart(product_name):
        # Ждём, что среди строк с классом success есть строка с текстом product_name
        browser.all("tr.success").element_by(have.text(product_name)).should(be.visible)

    @staticmethod
    @allure.step("Открываем окно регистрации")
    def open_sign_up_window():
        browser.element("#signin2").should(be.visible).click()
