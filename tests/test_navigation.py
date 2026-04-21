import allure

class TestNavigation:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_recovery_password_page(self,main_page,login_page):
        main_page.open_main_page_stellarburgers()
        main_page.click_personal_account_button()
        login_page.click_recover_password_button()

        assert login_page.check_open_recorev_password_page()

    @allure.title("Переход по клику на «Личный кабинет» НЕ авторизованным пользователем")
    def test_open_personal_accont_page_not_authorized_user(self, main_page, login_page):
        main_page.open_main_page_stellarburgers()
        main_page.click_personal_account_button()

        assert login_page.check_availability_autorisation_form()

    @allure.title("Переход по клику на «Личный кабинет» авторизованным пользователем")
    def test_open_personal_accont_page_authorized_user(self,main_page,authorized_user,personal_account_page):
        main_page.click_personal_account_button()

        assert personal_account_page.check_open_personal_account_page()
          
    @allure.title("Переход по клику в раздел «История заказов»")
    def test_open_orders_history_page(self, main_page, personal_account_page,authorized_user):
        main_page.click_personal_account_button()
        personal_account_page.click_orders_history_button()

        assert personal_account_page.check_open_orders_history_page()

    @allure.title("Переход по клику в раздел «Конструктор»")
    def test_open_constructor_page(self, main_page, constructor_page,authorized_user):
        main_page.click_order_feed_button()
        main_page.click_constructor_button()

        assert constructor_page.check_open_constructor_page()

    @allure.title("Переход по клику в раздел «Лента заказов»")
    def test_open_orders_feed_page(self, main_page, feed_orders_page,authorized_user):
        main_page.click_order_feed_button()
        
        assert feed_orders_page.check_open_feed_orders_page()




