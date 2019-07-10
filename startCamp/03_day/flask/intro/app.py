from flask import Flask, render_template
import datetime
import hello
import random
print(hello.message)
app = Flask(__name__)

@app.route('/') #데코레이터 @가 붙어있음 endpoint
def hello(): #hello 함수 return값 = Hello PARK!
    return render_template('index.html')


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
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return render_template('cube.html', html_num=num, html_result=result)


#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '고추짬뽕', '아무거나', '라면']
    sel = random.sample(menu, people)
    return str(sel)


@app.route('/movie')
def movie():
    movies = ['스파이더맨', '엔드게임', '기생충', '알라딘']
    return render_template('movie.html', movies=movies)
#파이썬 파일들은 모두 모듈이다. 따라서 import hello -> print(hello.message)
if __name__ == '__main__' : #name이라는 변수에 main이 담긴다
    app.run(debug=True)
