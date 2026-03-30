# opening a website in new window

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver =webdriver.Chrome()

driver.maximize_window()
sleep(2)

driver.switch_to.new_window('window')
sleep(2)
driver.get("https://www.cricbuzz.com/")

driver.switch_to.new_window('tab')
sleep(2)
driver.get("https://www.cricbuzz.com/")

