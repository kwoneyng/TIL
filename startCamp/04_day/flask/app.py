from flask import Flask, render_template, request #사용자의 요청을 확인할 수 있음
import requests

app = Flask(__name__)

@app.route('/')     #사용자가 들어올 수 있는 경로 생성 # / = root
def index():
    return 'Hello world'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age : {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    # Ascii Art API를 활용해서 사용자의 input값 변경
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)


@app.route('/lotto_input')
def lotto_input():
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    lotto_numbers = list(map(int,request.args.get('numbers').split()))
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # json 타입의 파일을 python dictionary로 parsing 해준다
    print(lotto_numbers)
    abso = []
    count = 0
    abso.append(lotto_info['drwtNo1'])
    abso.append(lotto_info['drwtNo2'])
    abso.append(lotto_info['drwtNo3'])
    abso.append(lotto_info['drwtNo4'])
    abso.append(lotto_info['drwtNo5'])
    abso.append(lotto_info['drwtNo6'])
    bnus_num = lotto_info['bnusNo']
    print(abso)
    print(lotto_round)
    for i in lotto_numbers :
        if i in abso :
            count = count + 1


    return f'{count}개 맞췄습니다'



if __name__ == '__main__':
    app.run(debug=True)
