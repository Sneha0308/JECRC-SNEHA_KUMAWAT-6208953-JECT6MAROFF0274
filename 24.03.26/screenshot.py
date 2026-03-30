import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# it joins current directory and the folder u want
folder = os.path.join(os.getcwd(), 'screenshot')

# it will get the p-ath and join them
os.makedirs(folder,exist_ok=True)


driver =webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
action = ActionChains(driver)
sleep(3)

driver.save_screenshot(os.path.join(f"{folder}/full_page.png)"))
sleep(3)

ele = driver.find_element(By.XPATH,'(//div[@class="ADXRXN"])[22]/descendant::img')

# //img[contains(@alt,"Photo of a woman in a cherry-patterned")] -- another xpath

action.scroll_to_element(ele).perform()
sleep(2)

ele.screenshot(f'{folder}/cheery_red.png')
sleep(3)
