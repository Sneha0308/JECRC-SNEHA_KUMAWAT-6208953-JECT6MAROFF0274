from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()


wait_obj = WebDriverWait(driver,10)

action = ActionChains(driver)

women = wait_obj.until(EC.element_to_be_clickable((By.XPATH,'(//div[@class="desktop-navLink"])[2]')))
sleep(3)
action.move_to_element(women).perform()
sleep(3)
women.click()

catgry = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//li[@data-reactid="195"]')))


for i in range(0,5):
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)

print('task complete')

driver.quit()
