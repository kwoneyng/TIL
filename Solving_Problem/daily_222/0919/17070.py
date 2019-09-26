near = [[0,1], [1,0], [1,1]]
n = int(input())
bd = [list(map(int, input().split())) for i in range(n)]
rs = 0
stack = [[0,1,0]]
while stack:
    x, y, di = stack.pop()
    if x == n-1 and y == n-1:
        rs += 1
    else:
        if di == 0:
            if y+1 < n:
                if bd[x][y+1] == 0:
                    stack.append([x,y+1,0])
            if x+1 < n and y+1 < n:
                cnt = 0
                for dx, dy in near:
                    if bd[x+dx][y+dy] != 0:
                        cnt += 1
                if cnt == 0:
                    stack.append([x+1,y+1,2])
        elif di == 1:
            if x+1 < n:
                if bd[x+1][y] == 0:
                    stack.append([x+1,y,1])
            if x+1 < n and y+1 < n:
                cnt = 0
                for dx, dy in near:
                    if bd[x+dx][y+dy] != 0:
                        cnt += 1
                if cnt == 0:
                    stack.append([x+1,y+1,2])
        if di == 2:
            if y+1 < n:
                if bd[x][y+1] == 0:
                    stack.append([x,y+1,0])
            if x+1 < n:
                if bd[x+1][y] == 0:
                    stack.append([x+1,y,1])
            if x+1 < n and y+1 < n:
                cnt = 0
                for dx, dy in near:
                    if bd[x+dx][y+dy] != 0:
                        cnt += 1
                if cnt == 0:
                    stack.append([x+1,y+1,2])
print(rs)