import pytest
from selenium import webdriver
import requests
from generators import Generatorss
from urls import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.orders_feed_page import OrdersFeedPage
from pages.constructor_page import ConstructorPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        options = ChromeOptions()
        options.add_argument("--headless")  # Запуск без окна
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Если используете старую версию Selenium, может понадобиться executable_path
        driver = webdriver.Chrome(options=options)
        
    elif request.param == 'Firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")  # Запуск без окна для Firefox
        driver = webdriver.Firefox(options=options)

    driver.browser_name = request.param
    yield driver
    driver.quit()

"""
@pytest.fixture(params=['Chrome','Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.browser_name = request.param

    yield driver
    driver.quit()
"""

@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture()
def feed_orders_page(driver):
    feed_orders_page = OrdersFeedPage(driver)
    return feed_orders_page

@pytest.fixture()
def personal_account_page(driver):
    personal_account_page = PersonalAccountPage(driver)
    return personal_account_page

@pytest.fixture()
def constructor_page(driver: WebDriver) -> ConstructorPage:
    constructor_page = ConstructorPage(driver)
    return constructor_page


@pytest.fixture()
def user():
    body = Generatorss.generate_random_payload_for_register_new_user()
    response = requests.post(
                f"{BASE_URL}{API}{USER_URL}register", json=body)
    yield response.json(), response.status_code, body
    requests.delete(f"{BASE_URL}{API}{USER_URL}", headers={
        "Authorization": response.json().get("accessToken")
    })

@pytest.fixture
def authorized_user(main_page, login_page, user,constructor_page):
    main_page.open_main_page_stellarburgers()
    main_page.click_personal_account_button()
    _, _, body = user
    login_page.login(
        email=body.get("email"),
        password=body.get("password"))
    constructor_page.close_modal()
    
@pytest.fixture()
def user_with_order(authorized_user,constructor_page):
    constructor_page.add_buns_to_order()
    constructor_page.click_place_order_button()
    constructor_page.wait_invisible_order_9999()
    constructor_page.close_order_id_popup()
    constructor_page.close_modal()


