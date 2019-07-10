import csv
import bs4
import requests

url = 'https://www.bithumb.com/'
response = requests.get(url)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')
coins = soup.select('.coin_list tr')


    
with open('coin_data2.csv', 'w', encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    for coin in coins:
        coin_name = coin.select_one('.coin_list td p a strong').text.replace('NEW','').strip()
        coin_price = coin.select_one('.coin_list .sort_real').text.replace(',','').strip()
        data = (coin_name, coin_price)
        csv_writer.writerow(data)