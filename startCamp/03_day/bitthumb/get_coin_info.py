import csv
import bs4
import requests

url = 'https://www.bithumb.com/'
response = requests.get(url)
html = response.text
coin = bs4.BeautifulSoup(html, 'html.parser')
coin_name = coin.select('.coin_list td p a strong')
coin_price = coin.select('.coin_list .sort_real')
result = []
for i in range(0, len(coin_name)):
    coin_name[i].text : coin_price
    result.append([coin_name[i].text, coin_price[i].text])


with open('coin_data.csv', 'w', encoding="utf-8") as f:
    for i in range(0,len(coin_name)):
        f.write(f'{coin_name[i].text},{coin_price[i].text}\n')
