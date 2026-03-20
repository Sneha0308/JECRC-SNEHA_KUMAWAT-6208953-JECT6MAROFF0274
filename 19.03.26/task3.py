# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)


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
driver.get("https://amazon.in/")
driver.maximize_window()

wait_obj = WebDriverWait(driver, 6)

submit =wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-inner"]')))
submit.click()

search =wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search.send_keys("toys")


search4= wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="nav-flyout-searchAjax"]/descendant::div[@id="sac-suggestion-row-4"]')))
search4.click()

sort_dropdown =wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-dropdown-prompt"] ')))
sort_dropdown.click()

btn =wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="s-result-sort-select_4"]')))
btn.click()

driver.quit()