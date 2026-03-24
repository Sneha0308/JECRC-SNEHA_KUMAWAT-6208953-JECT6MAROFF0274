from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://vogue.com/')
driver.maximize_window()
sleep(1)

action = ActionChains(driver)
image = driver.find_element(By.XPATH,'(//div[@class="aspect-ratio--overlay-container"])[77]')
action.scroll_to_element(image).perform()
sleep(3)

for i in range(0,6):
    action.send_keys(keys.PAGE_UP).perform()
    sleep(2)

sleep(3)
driver.quit()