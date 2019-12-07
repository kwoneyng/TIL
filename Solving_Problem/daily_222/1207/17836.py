from collections import deque

near = [[-1,0], [0,1], [1,0], [0,-1]]

n,m,t = map(int,input().split())
bd = [list(map(int, input().split())) for i in range(n)]

normal = 999999999999999999
equip_gram = 0
for x in range(n):
    for y in range(m):
        if bd[x][y] == 2:
            gram = [x,y]
            equip_gram = abs(n-1-x)+abs(m-1-y)
get_gram = 0
def go():
    q = deque([[0,0]])
    time = 0
    global normal, equip_gram, get_gram
    while q:
        time += 1
        if time > t+1:
            return
        for i in range(len(q)):
            x,y = q.popleft()
            if x == n-1 and y == m-1:
                normal = time - 1
                return
            for a,b in near:
                xi, yi = x+a, b+y
                if 0 <= xi < n and 0 <= yi < m:
                    if bd[xi][yi] == 0:
                        bd[xi][yi] = 1
                        q.append([xi,yi])
                    elif bd[xi][yi] == 2:
                        equip_gram += time
                        q.append([xi,yi])
                        bd[xi][yi] = 1
                        get_gram = 1
go()
# print(normal)
if normal <= t:
    if get_gram == 1:
        print(min(normal,equip_gram))
    else:
        print(normal)
elif get_gram and equip_gram <= t:
    print(equip_gram)
else:
    print('Fail')