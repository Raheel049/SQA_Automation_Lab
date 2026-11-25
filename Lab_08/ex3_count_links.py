from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.wikipedia.org")
    
    # Locate all anchor (<a>) elements
    links = driver.find_elements(By.TAG_NAME, "a")
    
    print("Total linkes in wikipedia is: ",len(links))
    assert len(links) > 0, "No links found on web page"
finally:
    driver.quit()