#!/usr/bin/python3
#usage:searchImage.py <keyword>
#模仿手动点击保存图片的过程
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import sys,os
import requests
#检查输入
assert len(sys.argv)==2, 'usage:searchImage.py <some-message>'
#打开必应图片网站
browser=webdriver.Firefox()
browser.get('https://cn.bing.com/images/')
#输入关键字，等待查询结果出现
keyword=browser.find_element_by_xpath('//*[@id="sb_form_q"]')
keyword.click()
keyword.send_keys(u'%s' %(sys.argv[1]))
keyword.submit()
wait = ui.WebDriverWait(browser,10)
try:
    wait.until(lambda browser: browser.find_element_by_xpath('//*[@id="mmComponent_images_1"]//div/div/a[contains(@class,"iusc")]'))
except Exception as err:
    print(str(err))

aElem=browser.find_element_by_xpath('//*[@id="mmComponent_images_1"]//div/div/a[contains(@class,"iusc")]')
browser.get(aElem.get_attribute('href'))

#将前6个结果存入硬盘
for i in range(6):
   try:
       wait.until(lambda browser: browser.find_element_by_xpath('//*[@id="mainImageWindow"]//img[contains(@class,"focus")]'))
       imgElem=browser.find_element_by_xpath('//*[@id="mainImageWindow"]//img[contains(@class,"focus")]')
       imgUrl=imgElem.get_attribute('src')
       res=requests.get(imgUrl) 
       res.raise_for_status()
       imgFile=open(os.path.join('xkcd',str(sys.argv[1])+'_'+str(i)),'wb') 
       for chunk in res.iter_content(100000):
            imgFile.write(chunk)
       imgFile.close()
       #获取下一个页面
       browser.find_element_by_xpath('//*[@id="navr"]/span').click()
   except Exception as err:
       print(str(err))
