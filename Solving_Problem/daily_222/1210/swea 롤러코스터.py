from collections import deque
from heapq import heappop, heappush


for t in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        a,b = map(int,input().split())
        heappush(data,[-(a-1)/b, a, b])
    rs = 1
    for i in range(len(data)):
        rate, a, b = heappop(data)
        rs = (a*rs + b)%1000000007
    print(f'#{t+1} {rs}')
    
