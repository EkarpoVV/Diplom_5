import allure

class TestConstructorPage:

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_popup_for_ingredient_button(self, main_page,constructor_page):
        main_page.open_main_page_stellarburgers()
        constructor_page.click_ingedient_button()
        
        assert constructor_page.check_open_ingredient_detail_popup()

    @allure.title("Проверка закрытия модального окна с ингредиентами кликом по крестику")
    def test_close_ingredient_details_popup(self, main_page,constructor_page):
        main_page.open_main_page_stellarburgers()
        constructor_page.click_ingedient_button()
        constructor_page.click_ingedient_modal_close_button()
        
        assert constructor_page.check_close_ingredient_detail_popup()

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_add_ingredient_to_order_chenge_counter_value(self, main_page,constructor_page):
        main_page.open_main_page_stellarburgers()
        constructor_page.add_buns_to_order()
        
        assert int(constructor_page.get_order_counter()) > 0

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_user_can_place_order(self, constructor_page, authorized_user):
        constructor_page.add_buns_to_order()
        constructor_page.click_place_order_button()

        assert constructor_page.check_open_your_order_has_been_prepared_popup()

