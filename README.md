# Diplom часть 3
# Проект автоматизации тестирования приложения Stellarburgers фронтенд часть
Основа для написания автотестов — фреймворк pytest
Установить зависимости — pip install -r requirements.txt.
Команда для запуска — pytest -v.
Запуск автотестов и создание allure-отчета — pytest tests/ --alluredir=allure_results
Просмотр allure-отчета в браузере — allure serve allure_results


# Проект состоит из пяти групп тестов 

test_constructor_page.py - проверяет функционал страницы Конструктор

test_feed_order_page.py - проверяет функционал страницы Лента заказов

test_navigation.py Проверяет логотим перехода по страницам

test_login_page.py - проверяет функционал страницы Авторизации

test_personal_account_page.py - проверяет функционал страницы Личный кабинет