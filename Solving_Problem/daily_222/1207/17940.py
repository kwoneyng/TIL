from heapq import heappop, heappush

n, m = map(int, input().split())
company = []
for i in range(n):
    company.append(int(input()))

bd = [list(map(int,input().split())) for i in range(n)]

q = [[0,0,0]] # 환승, 시간, 노드
while q:
    
