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

# submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
# submit_button.click()

# time out  error exception agr 10 sec hogyi and vse bhi dega
#  wait for element until it givess

loading_circle = wait_obj.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__circle3')))

title_abc = driver.find_element(By.XPATH,'//span[text() ="ABC SHOWS, SPECIALS & MORE"]')

assert 'SPECIALS' in title_abc.text, 'the text not present'
print('working fine')

driver.quit()