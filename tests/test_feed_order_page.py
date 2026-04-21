import allure

class TestFeedOrdersPage:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_order_details_popup(self, main_page,constructor_page,feed_orders_page,authorized_user):
        main_page.click_order_feed_button()
        feed_orders_page.click_order_button()

        assert feed_orders_page.check_open_orders_details_popup()
    
    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_can_see_orders_in_orders_history_and_orders_feed_page(self,user_with_order,personal_account_page, main_page,feed_orders_page):
        main_page.click_personal_account_button()
        personal_account_page.click_orders_history_button()
        last_order_id_from_order_history = personal_account_page.get_last_order_number_from_history()
        main_page.click_order_feed_button()
        last_order_id_from_order_feed = feed_orders_page.get_last_order_number()
        
        assert last_order_id_from_order_history == last_order_id_from_order_feed
        
    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_counter_for_all_time_increase(self,authorized_user,main_page,feed_orders_page,constructor_page):
        main_page.click_order_feed_button()
        complited_orders_for_all_time = feed_orders_page.get_complited_orders_for_all_time_counter()
        main_page.click_constructor_button()
        constructor_page.add_buns_to_order()
        constructor_page.click_place_order_button()
        constructor_page.wait_invisible_order_9999()
        constructor_page.close_order_id_popup()
        main_page.click_order_feed_button()
        new_complited_orders_for_all_time = feed_orders_page.get_complited_orders_for_all_time_counter()
        
        assert new_complited_orders_for_all_time > complited_orders_for_all_time
        
    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_counter_for_today_increase(self,authorized_user,main_page,feed_orders_page,constructor_page):
        main_page.click_order_feed_button()
        complited_orders_today = feed_orders_page.get_complited_orders_for_today_counter()
        main_page.click_constructor_button()
        constructor_page.add_buns_to_order()
        constructor_page.click_place_order_button()
        constructor_page.wait_invisible_order_9999
        constructor_page.close_order_id_popup()
        main_page.click_order_feed_button()
        new_complited_orders_today = feed_orders_page.get_complited_orders_for_today_counter()
        
        assert new_complited_orders_today > complited_orders_today


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_new_order_number_appears_in_works_section(self,authorized_user,main_page,feed_orders_page,constructor_page):
        constructor_page.add_buns_to_order()
        constructor_page.click_place_order_button()
        #order_id = constructor_page.wait_invisible_order_9999()
        order_id = constructor_page.wait_text_absense1()
        constructor_page.close_order_id_popup()
        constructor_page.close_modal()
        main_page.click_order_feed_button()
        feed_orders_page.get_last_order_number()
        order_in_work = feed_orders_page.get_last_cooking_orders_number()

        assert order_id in order_in_work

