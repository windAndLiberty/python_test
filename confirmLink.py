#!/usr/bin/python3
#usage:confirmLink.py <a-given-url> 
import requests,bs4,sys,os
#检查输入
assert len(sys.argv)==2, 'usage:confirmLink.py.py <a-given-url>'
#下载该页面
res=requests.get(sys.argv[1])
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,features="html.parser")
#新建目录
os.makedirs(sys.argv[1],exist_ok=True)
#下载该页面的所有链接页面
aElems=soup.select('a')
assert len(aElems)!=0, 'There is no a-tag in the page which '+sys.argv[1]+' pointing.'
for i in range(len(aElems)):
    try:
       print('Opening '+aElems[i].get('href')+'……')
       refer=sys.argv[1]+aElems[i].get('href') if not aElems[i].get('href').startswith('/',1,2) else 'https:'+aElems[i].get('href')
       res=requests.get(refer)

       res.raise_for_status()

       newFile=open(os.path.join(sys.argv[1],'link'+str(i)),'wb')   
       for chunk in res.iter_content(100000):
          newFile.write(chunk)
       newFile.close()

    except Exception as err:
       print('error: '+str(err))
       #标记坏链接，错误码404
       if(res.status_code==requests.codes.not_found):
           print(aElems[i].get('href')+' can not find.')    
         