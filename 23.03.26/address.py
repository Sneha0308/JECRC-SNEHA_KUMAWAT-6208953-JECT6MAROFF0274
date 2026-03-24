
#  copying and pasting for address fields

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r'C:\Users\HP5CD\PycharmProjects\23.03.26\index.html')
driver.maximize_window()
action = ActionChains(driver)

present = driver.find_element(By.ID,'presentAddress')
permanent = driver.find_element(By.ID,'permanentAddress')


present.send_keys('JECRC,JAIPUR ,RJ')
sleep(2)

present.click()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
permanent.click()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(5)

print('successfully copied')
driver.quit()


