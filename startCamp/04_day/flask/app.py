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

if __name__ == '__main__':
    app.run(debug=True)
