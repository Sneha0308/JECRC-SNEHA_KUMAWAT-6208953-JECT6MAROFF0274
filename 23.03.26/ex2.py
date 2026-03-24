
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)


action = ActionChains(driver)

drag = driver.find_element(By.ID, 'draggable')
drop = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(drag, drop).perform()
sleep(3)

text = driver.find_element(By.XPATH, '(//div[@id ="droppable"]/child::p)[1]')

assert 'Dropped!' in text.text,'not drag'
print('dragged')


sleep(3)
