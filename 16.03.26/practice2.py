from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
gender = input("Enter your gender: ")
# if else condition for gender selection
if gender == "Male":
    driver.find_element(By.ID ,'male').click()
else:
    driver.find_element(By.ID ,'female').click()


days = driver.find_elements(By.XPATH ,'//div[@class ="form-check form-check-inline"]/input[@type ="checkbox"]')
for day in days:
    day.click()
    sleep(1)

    print(day.get_attribute('value'))

for j in days[::-1]:
    j.click()
    sleep(1)


sleep(5)
driver.quit()