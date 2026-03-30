from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(2)


# single iframe
# iframe = driver.find_element(By.ID, "singleframe")
# driver.switch_to.frame(iframe)
# sleep(2)
#
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
# sleep(5)


#  nested iframes

driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()

nested_iframe = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)


inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
sleep(5)


driver.switch_to.parent_frame()   #switch to parent frame
driver.switch_to.default_content()  #switch to default frame

