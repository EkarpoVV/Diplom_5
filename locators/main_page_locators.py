from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')

