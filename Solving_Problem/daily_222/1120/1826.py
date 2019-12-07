from heapq import heappop, heappush
from collections import deque

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
l, p = map(int,input().split())
# print(data)
q = []
charge = [0]*(l+1)

for a,b in data:
    charge[a] = b

cnt = 0
for i in range(1,l+1):
    p -= 1
    if p < 0:
        q = sorted(q,reverse=True)
        while q:
            p += q.pop(0)
            cnt += 1
            if p > 0:
                break
        else:
            if p < 0:
                print(-1)
                break
    if charge[i] > 0:
        q.append(charge[i])
else:
    print(cnt)
