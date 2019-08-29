c, r = map(int, input().split())
point = int(input())
bd = []
for row in range(r):
    bd.append([0 for i in range(c)])
no = 0
sr, sc = [r, 0]
if point > r*c :
    print(0)
else:
    while no < c*r:
        for i in range(r+2):
            if sr - 1 >= 0 :
                if bd[sr-1][sc] == 0:
                    no += 1
                    bd[sr-1][sc] = no
                    sr -= 1
                else :
                    break
            else :
                break
        for i in range(c+2):
            if sc + 1 < c:
                if bd[sr][sc+1] == 0:
                    no += 1
                    bd[sr][sc+1] = no
                    sc += 1
                else:
                    break
            else :
                break
        for i in range(r+2):
            if sr + 1 < r:
                if bd[sr+1][sc] == 0:
                    no += 1
                    bd[sr+1][sc] = no
                    sr += 1
                else : 
                    break
            else :
                break
        for i in range(c+2):
            if sc - 1 >= 0 :
                if bd[sr][sc-1] == 0:
                    no += 1
                    bd[sr][sc-1] = no
                    sc -= 1
                else:
                    break
            else:
                break
    for x in range(r):
        for y in range(c):
            if bd[x][y] == point:
                print(y+1, r-x)
