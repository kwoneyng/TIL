from pprint import pprint
near = [(-1,0), (0,1), (1,0), (0,-1)]
def su_set(i, ls):
    if len(ls) == m:
        ch_set.append(ls)
        return 0
    for j in range(i+1, len(virus)):
        if virus[j] not in ls: 
            su_set(j, ls+[virus[j]])



n, m = map(int,input().split())
bd = [list(map(int, input().split())) for i in range(n)]
print(bd)
virus = []
ch_set = []
for x in range(n):
    for y in range(n):
        if bd[x][y] == 2:
            virus.append([x,y])
for i in range(len(virus)):
    su_set(i, [virus[i]])
for i in ch_set:
    q = []
    n_bd = [i[:] for i in bd]
    vis = [[0]*n for i in range(n)]
    for j in i:
        q.append([0,j])
    while q:
        time, xy = q.pop(0)
        x, y = xy
        for dx, dy in near:
            xi = x+dx
            yi = y+dy
            xyi = [xi, yi]
            if 0 <= xi < n and 0 <= yi < n:
                if bd[xi][yi] == 0:
                    bd[xi][yi] = 2
                    q.append([time+1, xyi])
    


pprint(ch_set)