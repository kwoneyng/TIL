from flask import Flask
import datetime
import hello
import random
print(hello.message)
app = Flask(__name__)

@app.route('/') #데코레이터 @가 붙어있음 endpoint
def hello(): #hello 함수 return값 = Hello PARK!
    return 'Hello PARK!'

@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 11, 26)
    td = b_day - today
    return f'{td.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines(): 
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

@app.route('/greeting/IU')
def greeting_IU():
    return '반갑습니다 IU님'

@app.route('/greeting/zionT')
def greeting_zionT():
    return '반갑습니다 zionT님'
    
#Variable Routing
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name} 님!'

@app.route('/cube/<int:num>')
def cube(num):
    return f'{num}의 3 제곱은 {num**3} 입니다.'

#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '고추짬뽕', '아무거나', '라면']
    sel = random.sample(menu, people)
    return str(sel)

#파이썬 파일들은 모두 모듈이다. 따라서 import hello -> print(hello.message)
if __name__ == '__main__' : #name이라는 변수에 main이 담긴다
    app.run(debug=True)
