import requests
import bs4

url = 'https://finance.naver.com/sise/'

response = requests.get(url) # response.text -> html
print(response)
print(response.status_code)
html = response.text #글자를 뽑아줘 request.get('주소').status_code -> 상태코드만 뽑아줘 ex(404error, 200(정상))

soup = bs4.BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text # id로 접근할 때는 #을 사용
print(kospi)

#.select(selector) 내용을 뽑아옴
#.select_ont(selector) 한개만 뽑아와