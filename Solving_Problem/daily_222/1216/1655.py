from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
su = []
rs = []
def insort(ls,st,ed,x):
    if st == len(su):
        ls.append(x)
        return
    if st > ed:
        ls[st:0] = [x]
    else:
        mid = (st+ed)//2
        if x > ls[mid]:
            insort(ls,mid+1,ed,x)
        elif x < ls[mid]:
            insort(ls,st,mid-1,x)
    

for i in range(n):
    insort(su,0,len(su),int(input()))
    mid = i//2
    if len(su) % 2 == 0:
        rs.append(str(min(su[mid], su[mid+1])))
    else:
        rs.append(str(su[mid]))

print('\n'.join(rs))
