from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    
    def open_url(self, url):
        """Navigate to the specific url"""
        self.driver.get(url)

    def find_element(self, locator):
        """Find a single web element"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find multiple web elements"""
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """Click on a web element"""
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Enter text into a input field"""
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retrieve text from a web element"""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator):
        """Check if an element is visible on the page"""
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False