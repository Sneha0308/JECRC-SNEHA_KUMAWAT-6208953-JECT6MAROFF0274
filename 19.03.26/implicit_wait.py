from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://abc.com")

driver.implicitly_wait(10)
# driver.find elemnts ke liye krega sare,  by default in seconds,global wait
# only usse to find element
# drawback --- it doesnt care weather it is visible or not
# after driver.get we can use it
# error-- no such elements find

# ele = driver.find_element(By.XPATH,'//a[@class ="AnchorLink"]/parent::li/descendant::span[3]')
# print(ele.text)

ele = driver.find_element(By.XPATH,'(//a[@class ="AnchorLink"]/parent::li/descendant::img)[1]')
print(ele.get_attribute('src'))
driver.quit()
