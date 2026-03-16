from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

search = driver.find_element(By.XPATH,'//form[@class ="lilxh_ header-form-search"]/descendant::input[@title="Search for Products, Brands and More"]')
search.clear()
search.send_keys("Mobiles",Keys.ENTER)

checkbox = driver.find_element(By.XPATH,'//div[@class="buvtMR"]')
checkbox.click()
print(checkbox.text)

image = driver.find_element(By.XPATH,'//div[@class="lWX0_T"]')
image.click()
print(image.get_attribute('src'))


#
# print(search.get_attribute('value'))
sleep(2)


driver.quit()
