import platform
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from videourl import url

options = Options()
if "--headless" in sys.argv:
    options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(url)
while (True):
    driver.find_element_by_class_name("likeButton").click()
    driver.refresh()
