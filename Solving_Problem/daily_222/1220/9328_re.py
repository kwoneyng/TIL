near = [[-1,0], [0,1], [1,0], [0,-1]]

def sc_etrc():
    ls = []
    for x in range(n):
        for y in range(m):
            if x == 0 or y == 0 or y == m-1 or x == n-1:
                if bd[x][y] != '*':
                    if ord('a') <= ord(bd[x][y]) <= ord('z'):
                        target = ord(bd[x][y]) - ord('a')
                        if key[target] == 2:
                            for i in needkey[target]:
                                ls.append(i)
                        key[target] = 1
                        ls.append([x,y])
                    elif ord('A') <= ord(bd[x][y]) <= ord('Z'):
                        target = ord(bd[x][y]) - ord('A')
                        if key[target] == 1:
                            ls.append([x,y])
                        else:
                            needkey[target].append([x,y])
                            key[target] = 2
                    else:
                        ls.append([x,y])
    return ls

def rupin():
    rs = 0
    vis = [[0]*m for i in range(n)]
    q = sc_etrc()
    for x,y in q:
        vis[x][y] = 1
    while q:
        x,y = q.pop(0)
        if bd[x][y] == '$':
            rs += 1
        for a,b in near:
            xi, yi = x+a, b+y
            if 0 <= xi < n and 0 <= yi < m:
                if bd[xi][yi] != '*' and vis[xi][yi] == 0:
                    if ord('a') <= ord(bd[xi][yi]) <= ord('z'):
                        target = ord(bd[xi][yi])-ord('a')
                        if key[target] == 2:
                            for a,b in needkey[target]:
                                q.append([a,b])
                                vis[a][b] = 1

                        key[target] = 1
                        q.append([xi,yi])
                        vis[xi][yi] = 1
                    elif ord('A') <= ord(bd[xi][yi]) <= ord('Z'):
                        target = ord(bd[xi][yi]) - ord('A')
                        if key[target] == 1:
                            q.append([xi,yi])
                            vis[xi][yi] = 1
                        else:
                            needkey[target].append([xi,yi])
                            key[target] = 2
                    else:
                        q.append([xi,yi])
                        vis[xi][yi] = 1
    print(rs)

for t in range(int(input())):
    n, m = map(int,input().split())
    bd=[list(input()) for i in range(n)]

    needkey = [[]for i in range(26)]
    key = [0]*26
    haven = list(input())
    for i in haven:
        if i == '0':
            break
        key[ord(i)-ord('a')] = 1

    rupin()
