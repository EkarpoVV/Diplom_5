from selenium.webdriver.common.by import By

class FeedOrdersLocators:
    FEED_ORDERS_PAGE = (By.XPATH, '//h1[text()="Лента заказов"]')
    LAST_ORDER = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]')
    ORDER_DETAIL_POPUP = (By.XPATH, '//p[text()="Cостав"]')
    LAST_ORDER_NUM = (By.XPATH, '(//p[contains(@class, "text_type_digits-default")])[1]')
    COMPLITED_ORDERS_FOR_ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COMPLITED_ORDERS_FOR_TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    LAST_COOKING_ORDERS = (By.XPATH, '(//ul[contains(@class, "OrderFeed_orderListReady__1YFem")])[1]')
    ALL_CURRENT_ORDERS_COMLETED = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')