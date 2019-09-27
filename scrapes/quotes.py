from bs4 import BeautifulSoup
import requests

res = requests.get('http://quotes.toscrape.com/')#for next page just change the url to http://quotes.toscrape.com/page/2

soup = BeautifulSoup(res.text,'lxml')

quote = soup.find_all('div',{'class':'quote'})


for q in quote:
    msg = q.find('span',{'class':'text'})
    print(msg.text)

    author = q.find('small')
    print("--"+author.text)
    print()

