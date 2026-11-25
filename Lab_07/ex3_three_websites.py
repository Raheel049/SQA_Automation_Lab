from selenium import webdriver
import time

driver = webdriver.Chrome()

try:

    # 01 Open three different website

    driver.get("https://www.google.com")
    print("site name", driver.title, "Url: ", driver.current_url)
    time.sleep(2)

    driver.get("https://www.github.com")
    print("Site name", driver.title, "Site URL: ", driver.current_url)
    time.sleep(3)

    driver.get("https://www.linkedin.com")
    print("Site name", driver.title, "Site URL ", driver.current_url)
    time.sleep(4)

    # Go back twice (linkedin ==> github ==> google)
    driver.back()
    driver.back()
    print("After back twice: ", driver.title)
    time.sleep(2)


    # Go forward once (google ==> github)
    driver.forward()
    print("After forward once: ", driver.title)
    time.sleep(2)

finally:
    # Close the window using quite
    driver.quit()