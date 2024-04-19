# selenium
 
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Firefox(executable_path= "/Documents/Learning Python/Projects/Python GPU bot/geckodriver.exe")
 
# enter keyword to search
#keyword = "geeksforgeeks"
 
# get geeksforgeeks.org
driver.get("https://store.nvidia.com/en-gb/geforce/store/gpu/?page=1&limit=9&locale=en-gb&category=GPU&gpu=RTX%203090")
 
# get element

element = driver.find_element(By.CLASS_NAME, "featured-container-lg")

# print complete element
print(element)

