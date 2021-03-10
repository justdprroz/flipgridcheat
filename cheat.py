import platform
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from videourl import url

def startBrowser():
    options = Options()
    if "--headless" in sys.argv:
        options.add_argument("--headless")
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=options)
    return driver

driver = startBrowser()
driver.get(url)
try:
    while True:
        driver.find_element_by_class_name("likeButton").click()
        driver.refresh()
except Exception as e:
    driver.close()
    print("CRASHED\n", e)


