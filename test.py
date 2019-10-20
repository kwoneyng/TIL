import requests
import bs4

url = 'https://github.com/bixbydevelopers/capsule-samples-collection'
response = requests.get(url=url)
print(response.json())

# soup = bs4.beautifulsoup(response, 'html.parser')
# print(soup)