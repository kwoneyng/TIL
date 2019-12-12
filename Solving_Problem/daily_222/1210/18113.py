from collections import deque
import sys
input = sys.stdin.readline
n,k,m = map(int, input().split())
data = deque()
mx = 0
for i in range(n):
    l = int(input())
    if l-2*k >= 0:
        if l-2*k ==0:
            continue
        data.append(l-2*k)
        mx += l-2*k
    elif l-k > 0:
        data.append(l-k)
        mx += l-k
e = mx//len(data)
for p in range(mx//m, 0, -1):
    cnt = 0
    for l in data:
        cnt += l//p
    if cnt >= m:
        print(p)
        break
else:
    print(-1)