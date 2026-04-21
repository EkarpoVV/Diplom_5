from selenium.webdriver.common.by import By

class LoginPageLocators:
    RECOVER_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    EMAIL_RECOVERY_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    RECOVERU_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    NEW_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]')
    SEE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.input__icon.input__icon-action svg')
    NEW_PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, '.input_status_active')
    RECOVER_PASSWORD_PAGE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD_FIELD =(By.CSS_SELECTOR, 'input[name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '.Auth_login__3hAey')  
    
