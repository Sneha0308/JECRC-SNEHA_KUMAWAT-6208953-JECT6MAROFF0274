from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

#  Open the form page
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(3)

driver.execute_script("document.body.classList.remove('modal-open')")
driver.execute_script("document.querySelectorAll('iframe').forEach(el => el.remove());")

#  Fill the form

# First Name
driver.find_element(By.ID, "firstName").send_keys("Sneha")

# Last Name
driver.find_element(By.ID, "lastName").send_keys("Kumawat")

# Email
driver.find_element(By.ID, "userEmail").send_keys("sneha858@test.com")

# Gender (Female)
driver.find_element(By.XPATH, "//label[@for='gender-radio-2']").click()

# Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# Subjects
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)

# Hobbies (Sports + Reading)
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']").click()

# Upload Picture (give your file path)
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\YourName\Pictures\test.png")

# Address
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")

# State
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

# City
driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

# 3. Click Submit
driver.find_element(By.ID, "submit").click()

time.sleep(3)

print("Form Submitted Successfully")

# Close browser
driver.quit()