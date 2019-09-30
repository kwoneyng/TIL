near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(x, y, result, cnt):
    global visit

    if cnt == 7:
        if result not in visit:
            visit.append(result)
            return

    else:
        for a, b in near:
            xi = x + a
            yi = y + b
            if 0 <= xi < 4 and 0 <= yi < 4:
                dfs(xi, yi, result+board[xi][yi], cnt+1)


for t in range(int(input())):
    board = [list(input().split()) for _ in range(4)]
    visit = []

    for i in range(4):
        for j in range(4):
            result = ''
            result += board[i][j]
            dfs(i, j, result, 1)
    print(visit)