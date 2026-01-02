from pages.login_page import LoginPage

def test_login_successfull(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver, "standard_user", "secret_sauce")
    login_page.login()