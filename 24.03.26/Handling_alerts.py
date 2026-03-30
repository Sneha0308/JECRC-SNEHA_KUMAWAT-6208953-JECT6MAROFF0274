# 1. simple alert -- single button or one tsk
# 2. conformation -- 2 option - cancel and ok
#  3. prompt alert -- have text filed

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(2)

# simple alert
# driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
# sleep(3)

 # conformation alert
#
# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.dismiss()
# alert.accept()
# sleep(3)

# prompt alert
# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.send_keys("querty")
#
# sleep(5)
# alert.accept()


wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)

