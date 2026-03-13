from selenium import webdriver
import time

browsers = [
    webdriver.Chrome,
    webdriver.Edge,
    webdriver.Firefox
]

for browser in browsers:
    driver = browser()
    driver.get("https://topbrains.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.quit()