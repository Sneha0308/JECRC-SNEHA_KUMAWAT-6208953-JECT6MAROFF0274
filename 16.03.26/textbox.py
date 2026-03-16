from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID,'name')
name.clear()
name.send_keys("Sneha")
sleep(5)

email = driver.find_element(By.XPATH,'//Input[@placeholder="Enter EMail"]')
email.send_keys("snehakumawat858@gmail.com")
sleep(5)

print(name.get_attribute('placeholder'))
print(name.get_attribute('value'))

# search = driver.find_element(By.ID,'twotabsearchtextbox')
# search.clear()
# search.send_keys("samsung26", Keys.ENTER)
# sleep(5)



driver.quit()