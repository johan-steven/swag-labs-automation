import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())

    my_driver = webdriver.Chrome(service=service)

    my_driver.implicitly_wait(10)
    my_driver.maximize_window()
    
    yield my_driver
    my_driver.quit()