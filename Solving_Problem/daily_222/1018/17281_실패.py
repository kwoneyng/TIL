from collections import deque
import itertools


def anta():
    global ground,rs
    ground.appendleft(1)
    a = ground.pop()
    if a == 1:
        rs += 1

def yeeruta():
    global ground,rs
    ground.appendleft(1)
    ground.appendleft(0)
    for i in range(2):
        if ground.pop() == 1:
            rs += 1

def samruta():
    global ground, rs
    ground.appendleft(1)
    ground.appendleft(0)
    ground.appendleft(0)
    for i in range(3):
        if ground.pop()==1:
            rs += 1
    
def homerun():
    global ground, rs
    rs += 1
    rs += sum(ground)
    ground = deque([0]*4)

def out():
    global ground, out_cnt
    out_cnt += 1


exe=[out,anta,yeeruta,samruta,homerun]
n = int(input())
each_in = deque()
for i in range(n):
    each_in.append(list(map(int,input().split())))
perm_set = list(itertools.permutations(list(range(1,9))))
mx = 0
for sunsu1 in perm_set:
    sunsu = list(sunsu1)
    sunsu[3:0] = [0]
    ground = deque([0]*4)
    start = 0
    out_cnt = 0
    rs = 0
    for i in range(n):
        while True:
            exe[each_in[i][sunsu[start]]]()
            start += 1
            start %= 9
            if out_cnt == 3:
                ground=deque([0]*4)
                out_cnt = 0
                break


    if mx < rs:
        mx = rs
print(mx)