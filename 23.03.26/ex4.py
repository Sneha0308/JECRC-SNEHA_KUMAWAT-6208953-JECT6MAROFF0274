
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r'C:\Users\HP5CD\PycharmProjects\23.03.26\index_2.html')
driver.maximize_window()
action = ActionChains(driver)

driver.find_element(By.ID,'password').send_keys('kumawat@1234')
sleep(2)
show_pwd = driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(2)
print(show_pwd.text)
action.release()