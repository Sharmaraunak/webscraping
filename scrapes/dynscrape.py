from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome("/usr/bin/google-chrome")

driver.get('https://www.hackerearth.com/challenges/')

#res = requests.get('https://www.hackerearth.com/challenges/')
res = driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

soup = BeautifulSoup(res,'lxml')

challeges = soup.find('div',{'class':'upcoming challenge-list'})

all_challenges = challeges.find_all('div',{'class':'challenge-card-modern'})

for challege in all_challenges:
    ctype = challege.find('div',{'class':'challenge-type'})
    name = challege.find('div',{'class':'challenge-name'})
    date = challege.find('div',{'class':'date'})

    print(ctype,name,date)