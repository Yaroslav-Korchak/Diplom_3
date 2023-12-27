import allure
from locators.personal_account_locators import *
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_to_element(AccountPageLocators.RESET_PASSWORD_LINK)