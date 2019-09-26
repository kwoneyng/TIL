from pprint import pprint

def go(x, y, color):
    for dx, dy in di:
        turn = []
        tx, ty = (x, y)
        while True:
            if 0 <= tx+dx < n and 0 <= ty+dy < n:
                tx += dx
                ty += dy
                if bd[tx][ty] == other:
                    turn.append([tx, ty])
                elif bd[tx][ty] == color:
                    while turn:
                        px, py = turn.pop(0)
                        bd[px][py] = color
                    break
                elif bd[tx][ty] == 0 or tx == 0 or ty == 0 or tx == n-1 or ty == n-1 :
                    turn = []
                    break
            else:
                break


for T in range(int(input())):
    n, m = map(int, input().split())
    bd = [[0]*n for i in range(n)]
    di = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for x in range(n//2-1, n//2+1):
        for y in range(n//2-1, n//2+1):
            if x == y :
                bd[x][y] = 2
            else :
                bd[x][y] = 1
    for i in range(m):
        x, y, color = list(map(int, input().split()))
        x -= 1
        y -= 1
        if color == 1:
            other = 2
        else :
            other = 1
        bd[x][y] = color
        go(x, y, color)
    rs_1 = 0
    rs_2 = 0
    for x in range(n):
        for y in range(n):
            if bd[x][y] == 1:
                rs_1 += 1
            elif bd[x][y] == 2:
                rs_2 += 1
    print('#{}'.format(T+1), rs_1, rs_2)