from pages.base_page import BasePage
import allure
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Кликнуть на кнопку Востановить пароль")
    def click_recover_password_button(self):
        self.click_to_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Вписать email для востановления пароля")
    def set_email_for_recover_password(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_RECOVERY_FIELD, email)

    @allure.step("Кликнуть на кнопку Восстановить")
    def click_recover_button(self):
        self.click_to_element(LoginPageLocators.RECOVERU_BUTTON)

    @allure.step("Указать новый пароль")
    def set_new_password(self, new_password):
        self.add_text_to_element(LoginPageLocators.NEW_PASSWORD_FIELD, new_password)

    @allure.step("Показать новый пароль")
    def show_new_password(self):
        self.click_to_element(LoginPageLocators.SEE_PASSWORD_BUTTON)
    
    @allure.step("Проверка активности поля новый пароль")
    def check_new_password_field_activity(self):
        try:
            self.find_element_with_wait(LoginPageLocators.NEW_PASSWORD_FIELD_ACTIVE)
            return True
        except:
            return False
        
    @allure.step("Заполнить поле Email")
    def set_email_field(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
    
    @allure.step("Заполнить поле Password")
    def set_password_field(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
    
    @allure.step("Кликнуть на кнопку Войти")
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверка доступности формы авторизации")
    def check_availability_autorisation_form(self):
        try:
            self.find_element_with_wait(LoginPageLocators.LOGIN_FORM)
            return True
        except:
            return False
        
    @allure.step("Залогиниться пользователем")
    def login(self, email, password):
        self.set_email_field(email)
        self.set_password_field(password)
        self.click_login_button()
    
    
    @allure.step("Проверка открытия страницы Восстановление пароля")
    def check_open_recorev_password_page(self):
        try:
            self.find_element_with_wait(LoginPageLocators.RECOVER_PASSWORD_PAGE)
            return True
        except:
            return False