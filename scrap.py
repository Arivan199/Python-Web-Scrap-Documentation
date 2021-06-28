import pandas as pd
from random import randint
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
driver=webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
titles,heads,news,strongs,photos,pdfs,vid=([],)*7
for page in links:
	driver.get(page)
	content=driver.page_source
	soup=BeautifulSoup(content,features='lxml')
	for a in soup.findAll('div',attrs={'class':'org-transparency-update'}):
		images=[]
		docs=[]
		videos=[]
		head=a.find('h1')
		boldnews=a.find('span')
		image=a.find('img')
		if not xxx is None:
			images.append("https:/tamilnet.com"+xxx)
		else:
			images.append(" ")
		for b in pdf:	
			xxx=b.find('a')
			docs.append("https:/tamilnet.com"+xxx.attrs['href'])
		vi=a.findAll('iframe')
		for b in vi:	
			xxx=b.get('src')
			videos.append(xxx)
		if not head is None:
			head=head.text
		heads.append(head)
		if not boldnews is None:
			boldnews=boldnews.text
		strongs.append(boldnews)
		photos.append(images)
		pdfs.append(docs)
		vid.append(videos)
	sleep(randint(1,3))
photos=pd.DataFrame(photos)
dc=pd.DataFrame(pdfs)
abc=pd.DataFrame(vid)
df=pd.DataFrame({'Date':dates,'News':titles,'LINK':links,'HEADLINE':heads,'NEWS HIGHLIGHT':strongs})
df1=pd.concat([df,photos,dc,abc],axis=1)
df1.to_csv('scrape2002-2005.csv')
