# to open chrome browser
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
sleep(13)
driver.get("https://supertails.com/")
sleep(13)
driver.maximize_window()
sleep(3)
driver.minimize_window()
sleep(2)

driver.back()
sleep(3)
driver.forward()
sleep(3)

opts = webdriver.FirefoxOptions()
opts.set_preference("detach", True)

# web browser apne aap bnd nhi hoga.

driver = webdriver.Firefox(options=opts)
driver.get("https://supertails.com/")
driver.maximize_window()

# driver.close()
# close a single window

driver.quit()
#  closes all the window  and cut connection

