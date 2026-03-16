from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# print title
print(driver.title)
sleep(2)

#locate username and clear if needed and enter username

username=driver.find_element(By.NAME, 'username')
username.clear()
username.send_keys("Admin")
sleep(3)


# Locate the password input field and enter the password using send_keys()
pswd=driver.find_element(By.NAME, 'password')
pswd.clear()
pswd.send_keys("admin123")
sleep(3)

# Submit the login form
driver.find_element(By.TAG_NAME, 'button').click()
sleep(3)


# url print
print(driver.current_url)
# dashboard is present or not

if "dashboard" in driver.current_url:
    print("Successful login")



driver.quit()