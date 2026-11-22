from selenium import webdriver
import time

driver = webdriver.Chrome()

siteName = ""

try:
    driver.get("https://www.github.com")
    print("Site name", driver.title)
    siteName = driver.title
    time.sleep(2)
    
    driver.refresh()
    print("Site name after the refresh:", driver.title)
    time.sleep(1)
    
finally:
    driver.quit()
    
print("siteName: ", siteName)
    