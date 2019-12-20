from collections import deque

near = [[-1,0], [0,1], [1,0], [0,-1]]


def entrance():
    ls = []
    for x in range(h):
        if bd[x][0] !='*':
            if bd[x][0] == '.' or bd[x][0] == '$':
                ls.append([x,0])
            elif ord('a') <= ord(bd[x][0]) <= ord('z'):
                if key[ord(bd[x][0])-kstd] == 2:
                    for i in plzop[ord(bd[x][0])-kstd]:
                        ls.append(i)
                key[ord(bd[x][0])-kstd] = 1
                ls.append([x,0])
            elif ord('A') <= ord(bd[x][0]) <= ord('Z'):
                if key[ord(bd[x][0])-ord('A')] == 1:
                    ls.append([x,0])
                else:
                    plzop[ord(bd[x][0])-ord('A')].append([x,0])
                    key[ord(bd[x][0])-ord('A')] = 2
        if bd[x][w-1] !='*':        
            if bd[x][w-1] == '.' or bd[x][w-1] == '$':
                ls.append([x,w-1])
            elif ord('a') <= ord(bd[x][w-1]) <= ord('z'):
                if key[ord(bd[x][w-1])-kstd] == 2:
                    for i in plzop[ord(bd[x][w-1])-kstd]:
                        ls.append(i)
                key[ord(bd[x][w-1])-kstd] = 1
                ls.append([x,w-1])
            elif ord('A') <= ord(bd[x][w-1]) <= ord('Z'):
                if key[ord(bd[x][w-1])-ord('A')] == 1:
                    ls.append([x,w-1])
                else:
                    plzop[ord(bd[x][w-1])-ord('A')].append([x,w-1])
                    key[ord(bd[x][w-1])-ord('A')] = 2

    for y in range(w):
        if bd[0][y] !='*':
            if bd[0][y] == '.' or bd[0][y] == '$':
                ls.append([0,y])
            elif ord('a') <= ord(bd[0][y]) <= ord('z'):
                if key[ord(bd[0][y])-kstd] == 2:
                    for i in plzop[ord(bd[0][y])-kstd]:
                        ls.append(i)    
                key[ord(bd[0][y])-kstd] = 1
                ls.append([0,y])
            elif ord('A') <= ord(bd[0][y]) <= ord('Z'):
                if key[ord(bd[0][y])-ord('A')] == 1:
                    ls.append([0,y])
                else:
                    plzop[ord(bd[0][y])-ord('A')].append([0,y])
                    key[ord(bd[0][y])-ord('A')] = 2
        if bd[h-1][y] !='*':        
            if bd[h-1][y] == '.' or bd[h-1][y] == '$':
                ls.append([h-1,y])
            elif ord('a') <= ord(bd[h-1][y]) <= ord('z'):
                if key[ord(bd[h-1][y])-kstd] == 2:
                    for i in plzop[ord(bd[h-1][y])-kstd]:
                        ls.append(i)
                key[ord(bd[h-1][y])-kstd] = 1
                ls.append([h-1,y])
            elif ord('A') <= ord(bd[h-1][y]) <= ord('Z'):
                if key[ord(bd[h-1][y])-ord('A')] == 1:
                    ls.append([h-1,y])
                else:
                    plzop[ord(bd[h-1][y])-ord('A')].append([h-1,y])
                    key[ord(bd[h-1][y])-ord('A')] = 2


    return ls

def rupin():
    rs = 0
    q = entrance()
    vis = [[0]*w for i in range(h)]
    while q:
        x,y = q.pop(0)
        if vis[x][y] == 1:
            continue
        vis[x][y] = 1
        if bd[x][y] == '$':
            rs += 1
        for a,b in near:
            xi, yi = x+a, y+b
            if 0 <= xi < h and 0 <= yi < w:
                if vis[xi][yi] == 0 and bd[xi][yi] != '*':
                    if bd[xi][yi] == '.':
                        q.append([xi,yi])
                    elif ord('a') <= ord(bd[xi][yi]) <= ord('z'):
                        target = ord(bd[xi][yi])-kstd
                        if key[target] == 2:
                            for i in plzop[target]:
                                q.append(i)
                        key[target] = 1
                        q.append([xi,yi])
                    elif ord('A') <= ord(bd[xi][yi]) <= ord('Z'):
                        target = ord(bd[xi][yi])-ord('A')
                        if key[target] == 1:
                            q.append([xi,yi])
                        else:
                            key[target] = 2
                            plzop[target].append([xi,yi])
                    elif bd[xi][yi] == '$':
                        rs += 1
                        vis[xi][yi] = 1
    print(rs)



for t in range(int(input())):
    h,w = map(int,input().split())
    plzop = [[] for i in range(26)]
    bd = [list(input()) for i in range(h)]
    have = list(input())
    key = [0]*(ord('z')-ord('a')+1)
    kstd = ord('a')
    dstd = ord('A')
    for i in have:
        if i == '0' :
            break
        key[ord(i)-kstd] = 1
    rupin()