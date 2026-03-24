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
action = ActionChains(driver)

action.send_keys(Keys.PAGE_DOWN).perform()
sleep(3)
action.send_keys(Keys.PAGE_UP).perform()
sleep(3)

action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(3)
action.key_up(Keys.CONTROL).perform()
sleep(3)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(3)




driver.quit()