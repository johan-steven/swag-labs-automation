from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_title_text(self):
        """Return the title text to verify that we entered."""
        return self.get_text(self.PAGE_TITLE)
    
    def add_to_cart_by_name(self, item_name):
        """The item name is formatted and the specific button for the item is clicked."""
        formatted_name = item_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{formatted_name}"

        add_button = (By.ID, button_id)
        self.click_element(add_button)
    
    def get_cart_count(self):
        """The number of items in the cart is obtained"""
        if self.is_element_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
    
    def go_to_cart(self):
        self.click_element(self.CART_ICON)