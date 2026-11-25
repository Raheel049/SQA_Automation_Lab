from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(1)
try:
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    
    # find all elements with type text
    text_input = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    print("Total input with the type text are :", len(text_input))
    
    # loop through each and print its identifying attribute
    for index, field in enumerate(text_input, start=1):
        field_id = field.get_attribute("id")
        field_name = field.get_attribute("name")
        print(f"Input {index} -> ID: '{field_id}', Name: '{field_name}'")
    
finally:
    driver.quit()