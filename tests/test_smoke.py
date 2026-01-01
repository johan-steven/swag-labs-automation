def test_browser_open(driver):
    driver.get("https://www.google.com")
    print(driver.title)