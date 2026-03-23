from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r"C:\Users\HP5CD\PycharmProjects\20.03.26\playlist.html")
driver.maximize_window()

songs_list = driver.find_element(By.ID,'songs')
select = Select(songs_list)

# if select.is_multiple:
#     for i in select.options:
#         if i.text.__contains__("Girl"):
#             select.select_by_visible_text(i.text)
#         elif i.text.__contains__("Love"):
#             select.select_by_visible_text(i.text)
if select.is_multiple:
    for i in select.options:
        assert "Girl" in i.text or "Love" in i.text
        select.select_by_visible_text(i.text)

driver.quit()
