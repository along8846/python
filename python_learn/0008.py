import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/explore'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

#for link in soup.find_all('a', class_='question_link'):
#    print(link.text)

for link in soup.find_all():
        print(link.get('href'))