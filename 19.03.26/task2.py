from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

# from explicity_wait import wait_obj

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=opts)
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()


wait_obj = WebDriverWait(driver,6)
name = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="username"]')))
name.send_keys("Sneha kumawat")


email = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))
email.send_keys("Snehakumawat858@gmail.com")

Tel = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="tel"]')))
Tel.send_keys("8567412365")


# Fax = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fax"]')))
# Fax.send_keys("1542547")
# sleep(3)


Files= wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@multiple="multiple"]')))
Files.send_keys(r"C:\Users\HP5CD\PycharmProjects")


gender = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//option[@value="female"]')))
gender.click()

exper = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@name="experience"][1]')))
exper.click()


skills = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="ip"][2]')))
skills2 = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="ip"][3]')))
skills3 = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="ip"][1]')))
skills.click()
skills2.click()
skills3.click()



Tools = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//option[@value="selenium"]')))
Tools.click()


submit =wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="submit"]')))
submit.click()


print("submit successfully")




