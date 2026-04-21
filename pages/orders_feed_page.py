from pages.base_page import BasePage
import allure
from locators.feed_order_locators import FeedOrdersLocators

class OrdersFeedPage(BasePage):

    @allure.step("Проверка открытия страницы Лента заказов")
    def check_open_feed_orders_page(self):
        try:
            self.find_element_with_wait(FeedOrdersLocators.FEED_ORDERS_PAGE)
            return True
        except:
            return False

    @allure.step("Кликнуть на заказ")
    def click_order_button(self):
        self.click_to_element(FeedOrdersLocators.LAST_ORDER)

    @allure.step("Проверка открытия модального окна с деталями заказа")
    def check_open_orders_details_popup(self):
        try:
            self.find_element_with_wait(FeedOrdersLocators.ORDER_DETAIL_POPUP)
            return True
        except:
            return False

    @allure.step("Получить номер последнего заказа из Ленты заказов")
    def get_last_order_number(self):
        return self.get_text_from_element(FeedOrdersLocators.LAST_ORDER_NUM)
    
    @allure.step("Получить количество заказов вывполненных за все время")
    def get_complited_orders_for_all_time_counter(self):
        return self.get_text_from_element(FeedOrdersLocators.COMPLITED_ORDERS_FOR_ALL_TIME_COUNTER)
   
    @allure.step("Получить количество заказов вывполненных за сегодня")
    def get_complited_orders_for_today_counter(self):
        return self.get_text_from_element(FeedOrdersLocators.COMPLITED_ORDERS_FOR_TODAY_COUNTER)
    
    @allure.step("Получить последний номер заказа из списка В работе")
    def get_last_cooking_orders_number(self):
        last_orderr_id = 'Все текущие заказы готовы!'
        while last_orderr_id == 'Все текущие заказы готовы!':
            last_orderr_id = self.get_text_from_element(FeedOrdersLocators.LAST_COOKING_ORDERS)
        return last_orderr_id
    
    @allure.step("Ждем исчезновения фразы Все текущие заказы готовы")
    def absense_text_all_current_orders_comleted(self):
        self.wait_text_absense(FeedOrdersLocators.ALL_CURRENT_ORDERS_COMLETED, "Все текущие заказы готовы!")

