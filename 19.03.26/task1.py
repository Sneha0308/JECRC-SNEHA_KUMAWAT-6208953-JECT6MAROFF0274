from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)


driver = webdriver.Chrome()
driver.get("https://abc.com/")
driver.maximize_window()


wait_obj = WebDriverWait(driver,10)

banner= wait_obj.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id ="hero-items"]/descendant::picture/descendant::img')))

for img in banner:
    print(img.get_attribute("src"))




driver.quit()