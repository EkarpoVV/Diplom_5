import allure

class TestPersonalAccount:

    @allure.title("Востановление пароля")
    def test_recover_password(self, main_page, login_page,personal_account_page,user,constructor_page):
        main_page.open_main_page_stellarburgers()
        main_page.click_personal_account_button()
        _, _, body = user
        login_page.set_email_field(body.get("email"))
        login_page.set_password_field(body.get("password"))
        login_page.click_login_button()
        constructor_page.close_modal()
        main_page.click_personal_account_button()
        personal_account_page.click_orders_history_button()
        personal_account_page.click_logout_button()
        
        assert login_page.check_availability_autorisation_form()

    

