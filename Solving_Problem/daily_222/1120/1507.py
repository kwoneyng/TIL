from heapq import heappop, heappush

n = int(input())
path = [0]*(1000002)
for i in range(n):
    a,b = map(int,input().split())
    path[a] = b
l,p = map(int,input().split())
cnt = 0
q = []
for i in range(1,l+1):
    p -= 1
    if p < 0:
        while q:
            p -= heappop(q)
            cnt += 1
            if p >= 0:
                break
        else:
            if p < 0:
                print(-1)
                break
    if path[i] > 0:
        heappush(q,-path[i])
else:
    print(cnt)
