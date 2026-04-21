from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
from urls import *

class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку Личный кабинет")
    def click_personal_account_button(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Открыть главную страницу stellarburgers")
    def open_main_page_stellarburgers(self):
        self.go_to_url(BASE_URL)
    
    @allure.step("Кликнуть на кнопку Личный кабинет через JS")
    def click_personal_account_button_via_js(self):
        self.click_element_via_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку Конструктор")
    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку Лента заказов")
    def click_order_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    