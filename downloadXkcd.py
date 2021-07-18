#!/usr/bin/python3
#下载单张的xkcd网站的单张漫画
import requests,os,bs4
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
   #download tho page 
   print('downloading page %s ……' % url )
   res= requests.get(url)
   res.raise_for_status()
   soup=bs4.BeautifulSoup(res.text,features="html.parser")
   #find the url of the comic image
   comicElems=soup.select('#comic > img')
   if comicElems == []:
      print('could not find the single comic image. ')
   else:
      comicUrl=comicElems[0].get('src')
      #download the image
      print('Downloading image %s…… ' % (comicUrl))
      res=requests.get("http:"+comicUrl)
      res.raise_for_status()
      #save the image to ~/xkcd
      imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
      for chunk in res.iter_content(100000):
            imageFile.write(chunk)
      imageFile.close()
   preLink = soup.select('a[rel="prev"]')[0]
   url = 'http://xkcd.com' + preLink.get('href')
print('done')