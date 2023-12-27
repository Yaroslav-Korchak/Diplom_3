from selenium.webdriver.common.by import By


class AccountPageLocators:
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'  # Войти
    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'  # Восстановить пароль
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля
