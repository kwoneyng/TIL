import os

with open('ssafy.txt', 'r') as f :
    lines = f.readlines() # 각 라인을 read 해서 list로 생성해준다.
    a = len(lines)
   
lines.reverse() # list를 반대로 뒤집는 함수.

with open('reversed_ssafy.txt', 'w') as f:
    for i in range(0, a) :
        f.write(lines[a-i-1])

