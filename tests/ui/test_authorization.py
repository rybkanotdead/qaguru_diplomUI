import allure
from allure_commons.types import Severity

from config import settings
from project_test_demoblaze.pages.login_form import LoginForm
from project_test_demoblaze.pages.main_page import MainPage

main_page = MainPage()
login_form = LoginForm()


@allure.label("owner", "alina oga")
@allure.tag("UI")
@allure.tag("Authorization")
@allure.severity(Severity.BLOCKER)
@allure.title("Проверяем авторизацию пользователя")
def test_login():
    main_page.open_main_page()

    main_page.open_login_window()
    login_form.fill_user()
    login_form.click_login()

    main_page.should_have_registered(settings.USER_LOGIN)
