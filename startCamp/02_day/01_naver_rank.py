import bs4
import requests

url = 'https://www.naver.com'
# 아이디는 #으로 접근 클래스는 .으로 접근
selector = '.ah_l .ah_item .ah_a .ah_k'
response = requests.get(url)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')
rank = soup.select(selector)
for i in range(0, len(rank)) :
    print('{0} : {1}'.format(i+1,rank[i].text))