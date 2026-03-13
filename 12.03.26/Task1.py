from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
sleep(10)
driver.get("https://blinkit.com/")
sleep(13)


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://blinkit.com/")
driver.maximize_window()
sleep(5)
driver.minimize_window()
sleep(5)
driver.back()
sleep(5)
driver.forward()
sleep(5)
driver.refresh()
sleep(5)
driver.quit()
driver.close()