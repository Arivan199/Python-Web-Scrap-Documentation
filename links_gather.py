import pandas as pd
import re
import random
from bs4 import BeautifuSoup
from selenium import webdriver
def generatelinks(str1,str2,str3):
  link=[]
  for i in range(1997,2021):
    for j in range(1,12):
      li=str1+str(i)+str2+str(j)+str3
      link.append(li)
  return link

news=generatelinks("https://tamilnet.com/cat.html?catid=13&year=","&month=","&view=compact")
#call the driver function
driver=webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#now need to grep each news links from the above mentioned months
for page in news:
	driver.get(page)
	content=driver.page_source
	soup=BeautifulSoup(content,features="html_parser")
	for a in soup.findAll('td',attrs={'id':'mainColumn'}):
		new=a.findAll('div',attrs={'class':'article'})
		for b in new:
			xxx=b.find('a')
			links.append(xxx.get('href'))
	sleep(randint(1,3))
