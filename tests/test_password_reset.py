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

