from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open three webpages in sequence
try:
    driver.get("https://www.wikipedia.org")
    driver.get("https://en.wikipedia.org/wiki/Software_testing")
    driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")
    time.sleep(2)
    
    # Go back twice (Selenium_(software) ==> Software_testing ==> wikipedia)
    driver.back()
    driver.back()
    print("After twice back current page name", driver.title)
    time.sleep(1)
    
    # Go forward once
    driver.forward()
    print("After forward onace", driver.title)
    time.sleep(1)
    
finally:
    driver.quit()