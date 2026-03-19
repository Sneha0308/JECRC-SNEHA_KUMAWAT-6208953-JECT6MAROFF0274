from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)
driver = webdriver.Chrome()


driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)

eye=driver.find_element(By.ID,'lrd1')
# print(eye.text)

# assert 'EYEGLASSES' in eye.text, 'didnt fiind'
assert 'GLASSES'==eye.text,'didnt find'
print('success')
driver.quit()