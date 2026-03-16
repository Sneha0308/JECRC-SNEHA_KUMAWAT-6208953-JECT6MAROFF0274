from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

# open page
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()


# print title
print(driver.title)
sleep(2)

# locate yes button

yes_radio = driver.find_element(By.ID, 'yes_radio')
driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()

sleep(2)

result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result:", result.text)

print("Class:", yes_radio.get_attribute("class"))
print("ID:", yes_radio.get_attribute("id"))

print("Current URL:", driver.current_url)





driver.quit()