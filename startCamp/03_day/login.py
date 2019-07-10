import bs4
import requests

url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
response = requests.get(url)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')
IDinput = soup.select('#userId')
print(I)