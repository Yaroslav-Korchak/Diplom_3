import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import time


class TestMainPage:

    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    def test_popup_of_ingredient(self, driver):
        page = MainPage(driver)
        page.click_on_crator_bun()
        text = page.get_text_of_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        assert text == "Детали ингредиента"

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_ingredient_details_window(self, driver):
        page = MainPage(driver)
        page.click_on_crator_bun()
        page.click_cross_button()
        page.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        assert page.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_quantity = main_page.check_quantity_of_ingredients()
        main_page.add_filling_to_order()
        end_quantity = main_page.check_quantity_of_ingredients()
        assert end_quantity == '1' and start_quantity == '0'

    @allure.title('Проверка успешного создания заказа')
    def test_successful_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.find_my_element(MainPageLocators.BUN)
        main_page.add_bun_to_order()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.find_my_element(MainPageLocators.ORDER_NUMBER)
        assert main_page.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
