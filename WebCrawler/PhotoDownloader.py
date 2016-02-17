from pip._vendor import requests
import bs4
r=requests.get('https://www.python.org/downloads/release/python-343/')
soup=bs4.BeautifulSoup(r.text)
img_list=soup.find_all('img')
for i in img_list:
    print(i['src'])

