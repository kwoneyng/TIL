import os

with open('ssafy.txt', 'r') as f :
    lines = f.readlines()
    a = len(lines)
   
with open('reversed_ssafy.txt', 'w') as f:
    for i in range(0, a) :
        f.write(lines[a-i-1])
# with open('ssafy.txt', 'w') as f :
