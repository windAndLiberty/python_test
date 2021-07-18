#!/usr/bin/python3
#lucky.py---打开百度搜索的几个页面
import webbrowser, sys, bs4, requests, logging
logging.basicConfig(filename='loggingDog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
print('^-^ |:->|\'.\'')
assert len(sys.argv)>1,"usage:lucky.py some-string-to-search" 
res=requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

logging.debug(res.text)
#del
webbrowser.open('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
soup=bs4.BeautifulSoup(res.text,features="html.parser")
elems=soup.select('a')
#
logging.debug(str(type(res.text))+str(len(res.text)))
logging.debug(res.text)
logging.debug(str(type(elems))+str(len(elems)))
numOpen=min(5,len(elems))
for i in range(numOpen):
    webbrowser.open('http://baidu.com')#+elems[i].get('href'))
