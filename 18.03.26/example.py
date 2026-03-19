from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)
driver = webdriver.Chrome()


driver.get('https://www.ecosia.org/')
driver.maximize_window()
sleep(5)

# search = driver.find_element(By.ID, 'twotabsearchtextbox')
# search.send_keys('handbags' ,Keys.ENTER)
# print(search.text)
# sleep(5)

search_box = driver.find_element(By.NAME,"q" )
sleep(5)

driver.quit()
