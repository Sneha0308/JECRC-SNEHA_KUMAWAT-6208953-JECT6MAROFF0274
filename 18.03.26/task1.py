from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

# 1. Go to the website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# 2. Find "Checkboxes" using LINK_TEXT
checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Checkboxes link found")

# 3. Find "Drag and Drop" using PARTIAL_LINK_TEXT
drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("Drag and Drop link found")

# 4. Count number of <li> elements
list_items = driver.find_elements(By.TAG_NAME, "li")
print("Total <li> elements:", len(list_items))

# 5. Navigate to tables page
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)

# 6. XPath → Website for email "jdoe@hotmail.com"
website = driver.find_element(
    By.XPATH,
    "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]"
)
print("Website (jdoe):", website.text)

# 7. XPath → Delete link for Last Name "Bach"
delete_link = driver.find_element(
    By.XPATH,
    "//table[@id='table1']//td[text()='Bach']/following-sibling::td//a[text()='delete']"
)
print("Delete link for Bach found")

# 8. XPath → Second table using indexing
second_table = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table located")

# 9. XPath → Cell with $100.00 and its parent row
cell_100 = driver.find_element(By.XPATH, "//table[@id='table2']//td[text()='$100.00']")
parent_row = cell_100.find_element(By.XPATH, "./parent::tr")

print("Cell value:", cell_100.text)
print("Parent row text:", parent_row.text)

# Close browser
driver.quit()