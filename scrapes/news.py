from bs4 import BeautifulSoup
import requests

res = requests.get('https://timesofindia.indiatimes.com/')

soup = BeautifulSoup(res.text,'lxml')

news_box = soup.find('ul',{'class':'list8'})

all_news = news_box.find_all('a')

for news in all_news:
    print(news.text)
    print()