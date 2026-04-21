from pages.base_page import BasePage
import allure
from locators.personal_account_locators import PersonalAccountLocators
from locators.login_page_locators import LoginPageLocators

class PersonalAccountPage(BasePage):

    @allure.step("Кликнуть на кнопку История заказов")
    def click_orders_history_button(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Кликнуть на кнопку Выход")
    def click_logout_button(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step("Проверка доступности формы авторизации")
    def check_availability_autorisation_form(self):
        try:
            self.find_element_with_wait(LoginPageLocators.LOGIN_FORM)
            return True
        except:
            return False
    
    @allure.step("Проверка открытия страницы Личный кабинет авторизованным пользователем")
    def check_open_personal_account_page(self):
        try:
            self.find_element_with_wait(PersonalAccountLocators.PERSONAL_ACCONT_PAGE)
            return True
        except:
            return False

    @allure.step("Проверка открытия страницы История заказов")
    def check_open_orders_history_page(self):
        try:
            self.find_element_presence_with_wait(PersonalAccountLocators.ORDER_HISTORY_PAGE)
            return True
        except:
            return False
    
    @allure.step("Получить номер последнего заказа из Истории заказов")
    def get_last_order_number_from_history(self):
        return self.get_text_from_element(PersonalAccountLocators.GET_ORDER_NUMBER)
        