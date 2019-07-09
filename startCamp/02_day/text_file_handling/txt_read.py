f = open('ssafy.txt', 'r')
all_text = f.read() # all text 전체를 불러온다 (개행문자 포함!)
print(all_text)
f.close()

with open('with_ssafy.txt', 'r') as f :
    all_text = f.read()
    print(all_text)

with open('with_ssafy.txt','r') as f :
    lines = f.readlines()
    for line in lines :
        print(line.strip()) #처음과 끝의 개행이나 공백을 지워주는 함수 (print 자체에 개행문자)