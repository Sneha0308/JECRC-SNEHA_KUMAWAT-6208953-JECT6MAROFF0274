from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)

driver = webdriver.Chrome()
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)

search = driver.find_element(By.XPATH, '//input[@placeholder="What are you looking for?"]')
search.clear()
search.send_keys('computer lenses',Keys.ENTER)
sleep(5)


glasses_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(glasses_dropdown)
dropdown.select_by_value('saving')
sleep(5)

inner_text = driver.find_element(By.XPATH,'(//div[@class="sc-bf32d8a7-0 gOVKHN"])[1]/descendant::p[@class ="sc-23b7d3eb-2 dQrJBg"][1]')
print(inner_text.text)


driver.quit()