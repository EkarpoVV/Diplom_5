from pages.base_page import BasePage
import allure
from locators.constructor_page_locators import ConstructorLocators

class ConstructorPage(BasePage):
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingedient_button(self):
        self.click_to_element(ConstructorLocators.INGREDIENT_BUTTON)

    @allure.step("Кликнуть на крестик модального окна с деталями ингредиета")
    def click_ingedient_modal_close_button(self):
        self.click_to_element(ConstructorLocators.INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON)

    @allure.step("Кликнуть на кнопку Оформить заказ")
    def click_place_order_button(self):
        self.click_to_element(ConstructorLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить счетчик заказа")
    def get_order_counter(self):
        return self.get_text_from_element(ConstructorLocators.INGREDIENTS_COUNTER)
    
    @allure.step("Проверка открытия страницы Конструктор")
    def check_open_constructor_page(self):
        try:
            self.find_element_with_wait(ConstructorLocators.CREATE_BURGER_PAGE)
            return True
        except:
            return False
        
    @allure.step("Проверка открытия модального окна с деталями ингредиентов")
    def check_open_ingredient_detail_popup(self):
        try:
            self.find_element_with_wait(ConstructorLocators.INGREDIENT_DETAILS_MODAL)
            return True
        except:
            return False    
    
    @allure.step("Проверка закрытия модального окна с деталями ингредиентов")
    def check_close_ingredient_detail_popup(self):
        try:
            self.find_element_with_wait(ConstructorLocators.INGREDIENT_DETAILS_MODAL) == False
            return True
        except:
            return False
    
    @allure.step("Перенос булок в заказа")
    def add_buns_to_order_via_druganddrop(self):
        self.my_drag_and_drop(ConstructorLocators.INGREDIENT_BUTTON, ConstructorLocators.DRUG_BUN_HERE_TOP)

    @allure.step("Перенос булок в заказа для ff")
    def add_buns_to_order_via_druganddrop_ff(self):
        self.drag_and_drop_element_ff(ConstructorLocators.INGREDIENT_BUTTON, ConstructorLocators.DRUG_BUN_HERE_TOP)  
  
    @allure.step("Проверка открытия модального окна Ваш заказ начали готовить")
    def check_open_your_order_has_been_prepared_popup(self):
        try:
            self.find_element_with_wait(ConstructorLocators.YOUR_ORDER_HAS_BEEN_PREPARED)
            return True
        except:
            return False       
        
    @allure.step("Кликнуть закрыть пупап идентификатор заказа")
    def close_order_id_popup(self):
        self.click_element_via_js(ConstructorLocators.CLOSE_ORDER_ID_POPUP)

    @allure.step("Ждем получеения номера заказа")
    def wait_order_number(self):
        self.find_element_clickable_with_wait(ConstructorLocators.CLOSE_ORDER_ID_POPUP)
 
    @allure.step("Ждем достумности пупапа с ID заказом")
    def wait_availability_order_number_popup(self):
        self.invisibility_of_element(ConstructorLocators.OVERLAY)

    
    @allure.step("Ждем исчезновения номера заказа 9999")
    def wait_invisible_order_9999(self):
        number = '9999'
        while number == '9999':
            number = self.wait_text_absense(ConstructorLocators.ORDER_NUMBER_IN_POPUP, "9999")
        return number
    
    @allure.step("Закрыть модальное окно в chrome")
    def close_invisible_popup_for_chrome(self):
            self.close_modal()

    @allure.step("Закрыть невидимое модальное окно")
    def close_modal(self):
        try:
            self.find_element_with_wait(ConstructorLocators.MODAL_FF)
            if self.element_is_displayed(ConstructorLocators.MODAL_FF):
                close_button = self.find_element_with_wait(ConstructorLocators.MODAL_CLOSE_FOR_FF)
                self.click_to_element(close_button)
                self.wait_for_modal_closed(self.driver, ConstructorLocators.HEADER_ACCOUNT_PAGE)
        except Exception as e:
            print(f"Error closing modal: {e}")
    
    @allure.step('Перенос булок в заказ')
    def add_buns_to_order(self):
        if self.driver.browser_name == 'Chrome':
            self.add_buns_to_order_via_druganddrop()
        if self.driver.browser_name == 'Firefox':
            self.add_buns_to_order_via_druganddrop_ff()

    def wait_text_absense1(self):
        self.wait_text_absense(ConstructorLocators.ORDER_NUMBER_IN_POPUP, '9999')
        
        return self.get_text_from_element(ConstructorLocators.ORDER_NUMBER_IN_POPUP)