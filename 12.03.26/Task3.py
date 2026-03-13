from selenium import webdriver
import time

browsers = [
    webdriver.Chrome,
    webdriver.Edge,
    webdriver.Firefox
]

for browser in browsers:
    driver = browser()
    driver.get("https://parade.com/")
    print(f'Current_URL: {driver.current_url}')
    print(f'Title: {driver.title}')
    print(f'Author: {driver.name}')
    time.sleep(2)
    driver.quit()