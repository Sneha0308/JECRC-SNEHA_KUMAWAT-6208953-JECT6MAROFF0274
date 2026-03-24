# performing mouse action and keyboard actions

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
driver.maximize_window()
sleep(3)


action = ActionChains(driver)



original_ele = driver.find_element(By.ID, 'column-a')
target_ele = driver.find_element(By.ID, 'column-b')


action.drag_and_drop(original_ele, target_ele).perform()
sleep(2)


