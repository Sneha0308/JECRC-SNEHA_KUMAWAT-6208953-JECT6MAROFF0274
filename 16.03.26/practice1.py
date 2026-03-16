from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.lenskart.com/")
driver.maximize_window()

search = driver.find_element(By.XPATH,'//Input[@placeholder="What are you looking for?"]')
search.clear()
search.send_keys("computer lens",Keys.ENTER)

# search_button = driver.find_element
# jisme enter nhi hoga usme button use krenge
sleep(5)

print(search.get_attribute('placeholder'))


driver.quit()
