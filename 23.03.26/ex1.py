
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get('https://supertails.com/')
driver.maximize_window()
sleep(3)


action = ActionChains(driver)

dogesh_bhai= driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
sleep(3)
action.move_to_element(dogesh_bhai).perform()
sleep(3)

driver.quit()