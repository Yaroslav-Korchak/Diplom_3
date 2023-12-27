import allure
from data.data import Urls
from locators.password_reset_locators import PasswordResetLocators
from pages.personal_account_page import PersonalAccountPage
from pages.password_reset_page import PasswordResetPage


class TestPasswordReset:
    @allure.title('Проверка перехода по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        page = PersonalAccountPage(driver)
        page.open_link(Urls.login_page)
        page.click_password_reset_link()
        current_url = page.get_current_url()
        assert current_url == Urls.forgot_password_page

    @allure.title('Проверка ввода почты и перехода после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, driver, create_and_delete_user):
        page = PasswordResetPage(driver)
        page.open_link(Urls.forgot_password_page)
        page.set_email_for_reset_password(create_and_delete_user[0]['email'])
        page.click_reset_button()
        page.find_my_element(PasswordResetLocators.SAVE_BUTTON)
        current_url = page.get_current_url()
        assert current_url == Urls.reset_password_page

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_enter_email_and_click_reset(self, driver, create_and_delete_user):
        page = PasswordResetPage(driver)
        page.open_link(Urls.forgot_password_page)
        page.set_email_for_reset_password(create_and_delete_user[0]['email'])
        page.click_reset_button()
        page.find_my_element(PasswordResetLocators.SAVE_BUTTON)
        page.click_on_show_password_button()
        assert page.find_my_element(PasswordResetLocators.INPUT_ACTIVE)
