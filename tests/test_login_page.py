import allure

class TestLoginPage:

    @allure.title("Восстановление пароля")
    def test_recover_password(self, main_page, login_page,constructor_page):
        main_page.open_main_page_stellarburgers()
        main_page.click_personal_account_button()
        login_page.click_recover_password_button()
        login_page.set_email_for_recover_password('maillll@ma.ru')
        login_page.click_recover_button()
        constructor_page.close_modal()
        login_page.show_new_password()

        assert login_page.check_new_password_field_activity()

    
