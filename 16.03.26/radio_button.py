from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, 'male').click()
driver.find_element(By.XPATH,'//label[@text()="Monday"]/preceding-sibling::input').click()

monday_checkbox = driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label').click()
print(monday_checkbox.text)

# tuesday_checkbox =driver.find_element(By.XPATH,'//input[@id="tuesday"]/following-sibling::label').click()
# print(tuesday_checkbox.text)


