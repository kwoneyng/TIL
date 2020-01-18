near = [[-1,0], [0,1], [1,0], [0,-1]]

def start(ls,s):
    if len(ls) == 7 and 3 < s < 7:
        ls.sort()
        rs.add(ls)
        return

    if len(ls)-4 > s:
        return

    for x,y in ls:
        for a,b in near:
            xi, yi = a+x, b+y
            if 0 <= xi < 5 and 0 <= yi < 5:
                if bd[xi][yi] == 'S':
                    start(ls+[[x,y]], s+1)
                else:
                    start(ls+[[x,y]], s)

rs = set()
bd = [list(input())]
for x in range(5):
    for y in range(5):
        if bd[x][y] == 'S':
            start([(x,y)],s)