#!/usr/bin/python3
#usage:play2048.py 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
driver=webdriver.Firefox()
driver.get('https://gabrielecirulli.github.io/2048/')
wait = ui.WebDriverWait(driver,10)
try:
   wait.until(lambda driver: driver.find_element_by_xpath('/html'))
except Exception as err:
   print(str(err))
htmlElem=driver.find_element_by_tag_name('html')
print('Html is loaded.')
while True:
   try:
     driver.find_element_by_xpath('/html/body//div[contains(@class,"game-over")]')
     break
   except:
     htmlElem.send_keys(Keys.UP)
     htmlElem.send_keys(Keys.RIGHT)
     htmlElem.send_keys(Keys.DOWN)
     htmlElem.send_keys(Keys.LEFT)
print('done.')