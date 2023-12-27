import allure
from locators.password_reset_locators import PasswordResetLocators
from pages.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text_to_element(PasswordResetLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        self.click_to_element(PasswordResetLocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.click_to_element(PasswordResetLocators.SHOW_PASSWORD_BUTTON)
