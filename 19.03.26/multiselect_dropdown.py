from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)


driver = webdriver.Chrome()
driver.get("https://demo.mobiscroll.com/select/multiple-select/")
driver.maximize_window()

multi_drop=driver.find_element(By.XPATH,'//select[@id="multiple-select-select"]')
select =Select(multi_drop)

if select.is_multiple():
    select.select_by_value('7')
    select.select_by_index(4)
    select.select_by_visible_text("Movies, Music & Games")

sleep(5)
select.deselect_all()
select.deselect_by_index(4)
print(select.first_selected_option)
print(select.all_selected_options)
driver.quit()
