
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(3)
# to the origin of the page
driver.execute_script("window.scrollTo(0,0);")
sleep(3)

# using scroll By
driver.execute_script("window.scrollBy(0,500);")# scrolling down 500px
sleep(2)
driver.execute_script("window.scrollTo(0,-200);") #scrolling up 200px from 500px
sleep(2)


# scrolling to element
ele= driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(2)

# clicking

click_ele= driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();',click_ele)
sleep(3)