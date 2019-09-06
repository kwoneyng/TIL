from pprint import pprint

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
pprint(ch_set)