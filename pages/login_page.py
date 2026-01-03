from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.username = username
        self.password = password

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self):
        self.enter_text(self.USERNAME_FIELD, self.username)
        self.enter_text(self.PASSWORD_FIELD, self.password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        print("Error...")