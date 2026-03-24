from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://supertails.com/')
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

cattu= driver.find_element(By.XPATH,'//div[@data-ganame = "Bread 5"]')
action.scroll_to_element(cattu).perform()
sleep(3)

action.scroll_by_amount(0,-1500).perform()
sleep(3)

#  scrolling top --- -ve
#  scrolling down -- +ve