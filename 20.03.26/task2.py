from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r"C:\Users\HP5CD\PycharmProjects\20.03.26\playlist.html")
driver.maximize_window()

multi_drop = driver.find_element(By.ID,'songs')
select1 = Select(multi_drop)




if select1.is_multiple:
    fav = driver.find_elements(By.XPATH, '//select[@id="songs"]/descendant::optgroup[8]')
    for i in fav:
        select1.select_by_visible_text(i.text)



print([i.text for i in select1.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()
sleep(5)
driver.quit()
