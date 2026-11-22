from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    # Maximize window for full desktop viewport testing
    driver.maximize_window()

    # First website
    driver.get("https://www.python.org")
    print("Website 1:", driver.title, "|", driver.current_url)
    time.sleep(1)

    # Second website
    driver.get("https://www.selenium.dev")
    print("Website 2:", driver.title, "|", driver.current_url)
    time.sleep(1)

    # Back, Forward, Refresh
    driver.back()
    print("After Back:", driver.title)
    time.sleep(1)

    driver.forward()
    print("After Forward:", driver.title)
    time.sleep(1)

    driver.refresh()
    print("After Refresh:", driver.title)
    time.sleep(1)

finally:
    driver.quit()