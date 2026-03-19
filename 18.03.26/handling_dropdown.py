#most of the time in select tag and gor this tag there is import select class
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# overlap na ho elements isly maximISE KA USE KRTE H

opts = webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(5)

country_dropdown = driver.find_element(By.ID,'country')

dropdown =Select(country_dropdown)

dropdown.select_by_value('australia')
sleep(5)

dropdown.select_by_index(4)
sleep(5)
dropdown.select_by_visible_text("Germany")

sleep(5)
driver.quit()