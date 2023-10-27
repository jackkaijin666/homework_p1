import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.4399.com/')
num = 100
a = 0
content = response.text
soup = BeautifulSoup((content),'html.parser')
images = soup.findAll('img')
print('100个4399游戏图标:')
for i in images:
    print(i)
    a = a+1
    if a>num:
        break
