from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time





driver_path = os.path.realpath('chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get('https://yandex.ru')
driver.maximize_window()
time.sleep(5)
driver.get('https://news.yandex.ru')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
