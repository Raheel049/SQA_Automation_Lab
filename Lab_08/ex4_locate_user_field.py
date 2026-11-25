from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # Strategy 1: By ID
    user_by_id = driver.find_element(By.ID, "username")
    print("1. Found using By.ID -> Tag:", user_by_id.tag_name)

    # Strategy 2: By NAME
    user_by_name = driver.find_element(By.NAME, "username")
    print("2. Found using By.NAME -> Type:", user_by_name.get_attribute("type"))

    # Strategy 3: By CSS Selector
    user_by_css = driver.find_element(By.CSS_SELECTOR, "input#username")
    print("3. Found using By.CSS_SELECTOR -> Success!")

    # Strategy 4 (Bonus): By Relative XPath
    user_by_xpath = driver.find_element(By.XPATH, '//input[@id="username"]')
    print("4. Found using By.XPATH -> Success!")

finally:
    driver.quit()