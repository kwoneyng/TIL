[TOC]



# Python

##### dictionary

```python
? = { '??' : '???'} : dict형태로 ?에 저장 '??'는 key값 '???'는 value값이다
? = dict(??='???') : 으로도 저장 할 수 있다.
?['??'] = '???'
```

```python
? = {
	'??1' : { 
		'??11' : '???11',
    	'??12' : '???12'   
	},
    '??2' : {
        '??21' : '???21',
        '??22' : '???22'
    }
}
dict안에 또 dict를 생성할 수 있다.
```

```python
# key, value 값 구하기
위의 dict에서
print(?[??1].keys()와 print(?[??2].values()를 실행 시키면)
dict_keys(['??11', '??12'])
dict_values(['???21', '???22'])을 얻을 수 있다.
a = list(?['??1'].values())  # ?['??1'] 밑의 value값들을 리스트화 시킬 수 있다.
print(a[1])을 통해 ???12 를 출력할 수 있다.
print(?.items())
#출력값
dict_items([('aa', {'aa11': 'aaa11', 'aa12': 'aaa12'}),
            ('bb', {'bb21': 'bbb21', 'bb22': 'bbb22'})])
각각 key와 value 값을 튜플로 나타내 준다.
```



##### def

```python
def ?(??,???='????'):  #default 값은 뒤에 항상 붙여줘야 한다
	???aaaaa???
    
?(bb, cc='??')  #가능
?(bb='??', cc)  #불가능
?(bb='??', cc='??')  #가능
```









##### format

```
# .format(?, ??) : 앞의 {}에 ?값을 넣어준다.
print('{0} 기준 : 서울시 {1}의 미세먼지 농도는 {2} 입니다'.format(time, location, dust))
```



##### io & 기본

```
a = input('?') : ?부분은 input 값의 도메인을 설명해주는 칸으로 사용
```

```
?.strip() : 개행문자를 제거해준다.
```

```
for ? in ?? : ??가 한번 순회할 때 까지 반복 ?
ex) for i in range(5) : 5번 반복
```

```python
# if문 형식 ?, ???은 조건 ??, ????, ????? 는 반환값
if ? :
    ??
elif ??? :
    ????
else :
    ?????
```

```python
#open
? = open('파일명', 'r')  #해당 파일을 읽는 생성자를 만든다
list = ?.read()  #읽어온 정보를 list로 바꾸어 저장한다.
?.close()  #항상 read 한 생성자를 닫아줘야 하며 이를 피하기 위해서 with문을 사용할 수 있다.

? = open('파일명', 'w')  #해당 파일에 덮어쓰기를 실행한다.
?.write(f'??')			#'w' 대신 'a' 로 바꾸면 추가 모드로 사용할 수 있다.
?.close()

```

```python
#with
with open('파일명', 'r') as ? :
    list = ?.read()
```

```python
#f string
print(f'{}?') : {}안에 변수를 사용할 수 있고 ?내용을 출력할 수 있다.
print(f'{??:.2f}') : ??값을 소숫점 둘째 자리까지 나타낸다
```

```python
#같지않다
a != b
a is not b
```

```python
#Test값 바로 for문 돌리기
for T in range(int(input())):
```

```python
#변수 for문 돌려서 작성
for i in range(int(input())):
	print(f'#{i+1}', end ='')  #print문이 끝나도 개행문자를 넣지 않음
	for k in range(len(?)):
    	print(f'?[k]', end=' ')  #for문에 따라 ?리스트의 0번 인덱스 부터 끝까지 한칸씩 띄고 작성
```









##### parse

```python
#list 정보를 int로 parse
a = list()
b = list(map(int,a)) 
```



##### list

```python
#list slicing
!list의 값이 str형 일 때 사용 가능. 숫자일 경우 memory error 발생한다.
list[?:??] : ?번 인덱스 부터 ??번째 직전 인덱스 까지
```

```python
#append
a = []
a.append(?) # 비어있는 리스트에 ?를 빈자리부터 채워준다.
```

```python
#마지막 idx
a[-1] #인덱스의 제일 마지막 값을 나타낸다.
```

```python
?.split('??') : ? 자료를 ??를 기준으로 끊어서 배열해준다.
```

```python
list? = list(map(int, input().split(?))) : ?을 기준으로 끊은 자료들을 int로 parse하여 list로 만들어줌
```

```python
reversed(list) : list의 순서를 반대로 바꾸어줌 list.reverse()로도 사용할 수 있다.
```

```python
a = '1234'
for i in a :
    print(i)		#문자형은 for문이 돌아간다.
```

```python
#zip
>>> list(zip([1, 2, 3], [4, 5, 6]))  #zip은 동일한 개수로 이루어진 자료형을 묶어준다
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```







##### import

```python
#os
os.chdir(r'path') : 작업하고 있는 위치 변경
list = os.listdir('path') : path안의 파일들의 이름을 list로 만들어준다.
list = os.path.splitext('파일명') : 파일이름을 끊어서 list로 만들어준다.
os.rename(?, ??) : 파일명이 ?인 것을 ??으로 바꿔준다.
os.system(?) : cmd창에서 ?문을 실행한다.
?.replace(??, ??) : ?에서 ??부분을 삭제하고 ???로 대체한다.
```

```python
#webbrowser
webbrowser.open(f'http://www.google.com/search?q={idol}')
: f를 넣으면 ''안쪽에서 변수를 이용할 수 있다. 변수는 {}안에 입력한다.
```

```python
#random
shuffle(list) # list를 섞어준다.
a = random.sample(list, ?) : list의 값들 중 랜덤으로 ?개 뽑아온다.
random.choice(list) : list의 값중 하나를 랜덤으로 뽑아온다.
```

```python
#bs4
list = bs4.BeautifulSoup(?,'html.parser') : ??내용을 html.parser를 통해 사용하기 용이하도록 태그의 형태로 끊어서 list에 저장한다.
? = ??.select(???) : ??에 저장되어있는 태그 중 ???에 해당하는 태그를 모두 가져온다.
  #select_one은 하나만 가져온다.
```

```python
#csv
!read
import csv
with open('파일명', 'r', encoding='?' , newline='??') as ??? :
    ???? = csv.reader(???)
    for i in ???? :
        print(i)
csv를 활용하여 파일을 읽어오고(r) ?으로 문자를 인코딩해주며 새로운 줄로 바뀔 때 ??를 첨부한다
생성자는 ???로 사용 할 수 있으며 csv.reader(???)를 통해 ????에 list형으로 저장된다

!write
with open('파일명', 'w', encoding='?' , newline='??') as ??? :
    f.write(f'')
    ???? = csv.writer(???)
    ????.writerow(list)
위와 동일하며 선택자는 csv.writer(???)를 통해 생성하고 ????.writerow를 통해 csv파일 형태로 만들 수 있다. 이 경우에는 writerow()가 받아오는 값이 list 형태이어야 한다
```

```python
#datetime
import datetime
? = datetime.datetime.now()  #현재 날짜를 ?에 저장
? = datetime.datetime(yyyy, mm, dd)  #작성한 날짜를 ?에 저장
```







##### page ref

```python
import bs4
url = 'https://www.naver.com'
selector = '?' # 찾고 싶은 값 id는 #로 접근하고 class는 .으로 접근한다.
response = request.get(url)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')
?? = soup.select(slector)
```





# Git

```
$ git init : 속성을 master로 만들어준다
```

레파지토리 주소 복사 -> remote 등록

```
$ git remote add origin '주소'
```

주소 등록되었는지 확인

```
$ git remote -v 
```

```
$ git add . : 현재 디렉토리 내의 모든 파일을 staging area에 올려준다
```

```
$ git commit -m "" : ""내용과 함께 git에 push할 준비를 함
```

```
$ git config --global user.name "Park"
```

```
$ git push origin master : commit한 내용을 git으로 옮김
```

```
$ git status : git의 현재 상태를 확인. 커밋할 목록에 담겨있는지 untracked인지 등 다양한 정보 제공
```

```
$ git log : 현재까지 커밋된 모든 이력을 확인할 수 있다.
```

```
$ git remote add origin __경로__ : 원격저장소를 origin이라는 이름으로 등록
```

```
$ git remote -v : 현재 등록된 원격 저장소를 확인할 수 있다.
```







# Git bash

```
$ touch '파일명' : 현재 디렉토리에 파일 생성
```

```
$ python '파일명' : 현재 디렉토리에 있는 python 파일 실행
```

```
$ cd '폴더명' : 해당 디렉토리로 변경
```

```
$ mkdir '폴더명' : 새로운 디렉토리 생성
```

```
$ echo '내용' : 내용 출력
```

```
$ rm '파일명' : 해당 파일 지우기
```

```
$ exit : 터미널 종료
```

```
$ code . : 현재 디렉토리 부터 vs코드를 실행시킨다.
```





# Typora

(# ?) : 헤드라인

(*?*) : *  * 이탤릭 (ctrl + i)

(**?**) : **  ** 볼드 (ctrl + b)

[   T O C   ]  : 목차 생성

```?``` : 코드 블록 생성

![이미지](?) : (까지 작성하였을 때 이미지를 첨부할 수 있다

ctrl + t : 표 삽입

- list ( - list ) : list 표시( 순서 X )

1. ( 1. ) : list 표시 (순서 O)

[주소]('url') ([주소] ('url')) : 'url'로 가는 링크를 주소에 걸어줌





# Flask

Resume 파일을 갱신하면 Github 주소로 들어갔을 때 내가 수정한 템플릿 페이지를 볼 수 있다.

```python
@app.route('/?')  #route 주소에서 ?만큼 요청했을 때 실행한다
def ?():  #? 함수를 정의한다.
    return ??  #??를 반환한다
```

```python
if __name__ = '__main__' :	#현재창 일 때 __name__ = __main__이므로 현재 창일때 app.run()실행
	app.run(debug=True)		#debug=Ture를 추가하였을 때 역동적인 서버로 바꾸어줌
```

```python
#render_template
@app.route('/?')
def ?():
    ?? = 변수
    return render_template('???', ????=??) #작동할 때 ???페이지로 이동시켜준다
#이동할 때 현재 페이지의 ??이라는 변수가 ???페이지에서 ????으로 사용할 수 있게 보내 줄 수 있다.
#여러개도 가능하다
```

