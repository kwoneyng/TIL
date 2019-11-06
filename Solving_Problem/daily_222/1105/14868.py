from collections import deque

near = [[-1,0],[0,1],[1,0],[0,-1]]

def debug():
    print('------------')
    for i in bd:
        print(i)
    print(ht)
    print(q)
    print('------------')

def spread(cul1,cul2):
    sumcul = ht[cul1]|ht[cul2]
    for i in ht[cul1]:
        ht[i] = sumcul
    for i in ht[cul2]:
        ht[i] = sumcul


def injub(x,y):
    global stop
    cul1 = bd[x][y]
    for a,b in near:
        xi, yi = x+a, y+b
        if 0 <= xi < n and 0 <= yi < n:
            cul2 = bd[xi][yi]
            if cul2 > 0 and cul1 != cul2:
                spread(cul1,cul2)
                if len(ht[cul1]) == k:
                    stop = 1
                    return

def moon():
    global year
    while True:
        year += 1
        for i in range(len(q)):
            x,y = q.popleft()
            cul1 = bd[x][y]
            for a,b in near:
                xi,yi = x+a, y+b
                if 0 <= xi < n and 0 <= yi < n:
                    cul2 = bd[xi][yi]
                    if cul2 == 0:
                        bd[xi][yi] = cul1
                        q.append([xi,yi])
                        injub(xi,yi)
                        if stop == 1:
                            print(year)
                            return
                    elif cul2 > 0 and cul1 != cul2:
                        spread(cul1,cul2)
                        if len(ht[cul1]) == k:
                            print(year)
                            return
                

n,k = map(int,input().split())
bd = [[0]*n for i in range(n)]
ht = {}
q = deque()
stop = 0
year = 0
for i in range(1,k+1):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    bd[x][y] = i
    q.append([x,y])
    ht[i] = set()
    ht[i].add(i)
    injub(x,y)
if stop == 0:
    moon()
else :
    print(0)