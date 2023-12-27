import pytest
from selenium import webdriver
# from locators.main_page_locators import MainPageLocators
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
