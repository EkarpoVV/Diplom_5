from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    CREATE_BURGER_PAGE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    PERSONAL_ACCONT_PAGE = (By.XPATH, '//p[text()="В этом разделе вы можете изменить свои персональные данные"]')
    ORDER_HISTORY_PAGE = (By.CSS_SELECTOR, '.OrderHistory_orderHistory__qy1VB')
    GET_ORDER_NUMBER = (By.CSS_SELECTOR, '.text_type_digits-default')