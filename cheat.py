import platform

from selenium import webdriver

from videourl import url

if platform.system() == "Linux":
    driver = webdriver.Chrome("./chromedriver")
if platform.system() == "Windows":
    driver = webdriver.Chrome("./chromedriver.exe")

driver.get(url)
while (True):
    driver.find_element_by_class_name("likeButton").click()
    driver.refresh()
