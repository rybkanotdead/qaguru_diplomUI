# Демонстрационный проект по тестированию UI и API сайта <a target="_blank" href="https://www.demoblaze.com">Product Store</a>
![This is an image](images/demoblaze.png)

## Стек технологий:
<img src="images/icons/python_logo_and_wordmark.svg" height="40" width="40"/><img src="images/icons/selenium.png" height="40" width="40"/><img src="images/icons/pytest_logo.svg" height="40" width="40"/><img src="images/icons/selene.png" height="40" width="40" /><img src="images/icons/selenoid.svg" height="40" width="40" /><img src="images/icons/requests.png" height="40" width="40" /><img src="images/icons/jenkins.svg" height="40" width="40" /><img src="images/icons/allure_Report.svg" height="40" width="40" /><img src="images/icons/telegram.svg" height="40" width="40" />

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