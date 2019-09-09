bd = [[0]*n for i in range(n)]
cross = [(1,1), (-1,1), (1,-1), (-1,-1)]
def pick(i, ls):
    global n, count
    if i > n:
        count += 1
        return
    for j in range(n):
        if bd[i][j] == 0:
            nls = ls
            for x in range(n):
                nls[x][j] = 1
            for y in range(n):
                nls[i][y] = 1
            for dx, dy in cross:
                while True:
                    i += dx
                    j += dy
                    if 0 <= X < n and 0 <= Y < n:
                        nls[X][Y] = 1
                    else :
                        break
            pick(i+1, nls)



for T in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        pick(i)