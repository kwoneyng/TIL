import sys
from collections import deque

def init():
    global rs
    for i in range(n):
        x = valid(data[i])
        if x:
            ht[x] = 1
        else:
            rs = 'NO'
            return
            
def valid(x):
    for i in range(len(x)):
        if ht.get(x[:i]):
            return
    return x


for t in range(int(input())):
    n = int(input())
    rs = 'YES'
    data = []
    for i in range(n):
        data.append(input())
    data.sort(key=lambda x: len(x))
    ht = {}
    init()
    print(rs)
