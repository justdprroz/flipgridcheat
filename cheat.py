import platform
import sys

from selenium import webdriver

if platform.system() == "Linux":
    driver = webdriver.Chrome("./chromedriver")
if platform.system() == "Windows":
    driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://flipgrid.com/12b8fe2f")
while (True):
    driver.find_element_by_class_name("likeButton").click()
    driver.refresh()
