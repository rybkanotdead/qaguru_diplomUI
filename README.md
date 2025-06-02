# Демонстрационный проект по тестированию UI и API сайта <a target="_blank" href="https://www.demoblaze.com">Product Store</a>
![This is an image](images/demoblaze.png)

## Проект реализован с использованием:
<img src="images/icons/python_logo_and_wordmark.svg" height="40" width="40"/><img src="images/icons/selenium.png" height="40" width="40"/><img src="images/icons/pytest_logo.svg" height="40" width="40"/><img src="images/icons/selene.png" height="40" width="40" /><img src="images/icons/selenoid.svg" height="40" width="40" /><img src="images/icons/requests.png" height="40" width="40" /><img src="images/icons/jenkins.svg" height="40" width="40" /><img src="images/icons/allure_Report.svg" height="40" width="40" /><img src="images/icons/telegram.svg" height="40" width="40" /><img src="images/icons/allure-testops.png" height="40" width="40"/>
- Дипломный проект выполнен на языке: `Python`
- Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
- Библиотека модульного тестирования: `PyTest`
- `Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер пользователя не требуется.
- Фреймворк`Allure Report` собирает графический отчет о прохождении тестов
- После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант Allure Report

## Для запуска тестов локально необходимо:
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/rybkanotdead/qaguru_diplomUI.git
```
```
cd qaguru_dimplom
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
- Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
- Если у вас Windows
    ```
    source venv/scripts/activate
    ```
Обновить pip:
```
pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Создать и заполнить .env файл, например:
```
touch .env
```
```
echo ENVIRONMENT='local' >> .env
```
```
echo USER_LOGIN='any_login' >> .env
```
```
echo USER_PASSWORD='any_password' >> .env
```
```
echo API_PASSWORD='any_api_password' >> .env
```
Запустить тесты:
```
pytest .
```
## <img title="Jenkins" src="images/icons/jenkins.svg" height="30" width="30"/> Jenkins
[![Button](https://img.shields.io/badge/Открыть%20сборку-d33732)](https://jenkins.autotests.cloud/job/qaguru_demoblazedip/49/allure/)
<details><summary>Результат выполнения</summary></details>
<br>
<details><summary>Общая информация</summary>
<br>
<img src="images/allureотчет.png">
</details>
<details><summary>Тест-кейсы</summary>
<br>
<img src="images/allure.png">
</details>
<details><summary>Видео прохождения тест-кейса</summary>
<br>
<img src="images/video.gif"></details>
<details><summary>Уведомление в telegram</summary>
<br>
<img src="images/telegram.png">
</details>

## <img title="Allure TestOps" src="images/icons/allure-testops.png" height="30" width="30"/> Allure TestOps

[![Button](https://img.shields.io/badge/Открыть%20проект-21c45e)](https://allure.autotests.cloud/project/4763/dashboards)
<details><summary>Общая информация</summary>
<br>
<img src="images/testops.png">
</details>

<details><summary>Тест-кейсы</summary>
<br>
<img src="images/testcase.png">
</details>

<details>
  <summary>История запусков</summary>
  <p>
    <img src="images/launch.png" alt="Launch History">
  </p>
</details>
