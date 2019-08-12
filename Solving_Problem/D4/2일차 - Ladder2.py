def go(ls, x, y):
    bd = ls[:]
    if x == 99:
        return 1
    near = [[0, 1],[0, -1],[1, 0]]
    for a,b in near:
        if 0 <= x+a < 100 and 0 <= y+b < 100 :
            if bd[x+a, y+b] == '1':
                bd[x+a, y+b] = '5'  
                if go(bd, x+a, y+b) == 1:
                    return 1
    return 0


for T in range(10):
    ladder = []
    n = int(input())
    for i in range(100):
        ladder.append(input().split())
    start = []
    for j in range(len(ladder[0])):
        if ladder[0][j] == '1':
            start.append([0, j])
    result = []
    for x, y in start:
        if go(ladder, x, y) == 1:
            print(y)
