from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    cell = driver.find_element(By.XPATH, '//table[@id="customers"]//tr[3]/td[2]')
    
    print("Text in 3rd row and 2nd column: ", cell.text)
    
finally:
    driver.quit()