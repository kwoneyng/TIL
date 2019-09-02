c, r = map(int, input().split())
point = int(input())
bd = []
for row in range(r):
    bd.append([0 for i in range(c)])
no = 0
sr, sc = [r, 0]
<<<<<<< HEAD
fin = True
while fin and no < c * r:
    for i in range(r+2):
        if sr - 1 >= 0 :
            if bd[sr-1][sc] == 0:
                no += 1
                if no == point:
                    print(sc+1, abs(r-sr-1))
                    fin = False
=======
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
>>>>>>> ee8de43198a6a586f4d01d7a0955a17ae6e7fd4c
                    break
            else :
                break
<<<<<<< HEAD
        else :
            break
    if not fin :
        break
    for i in range(c+2):
        if sc + 1 < c:
            if bd[sr][sc+1] == 0:
                no += 1
                if no == point:
                    print(sc+2, abs(r-sr))
                    fin = False
=======
        for i in range(c+2):
            if sc + 1 < c:
                if bd[sr][sc+1] == 0:
                    no += 1
                    bd[sr][sc+1] = no
                    sc += 1
                else:
>>>>>>> ee8de43198a6a586f4d01d7a0955a17ae6e7fd4c
                    break
            else :
                break
<<<<<<< HEAD
        else :
            break
    if not fin :
        break
    for i in range(r+2):
        if sr + 1 < r:
            if bd[sr+1][sc] == 0:
                no += 1
                if no == point:
                    print(sc+1, abs(r-sr+1))
                    fin = False
=======
        for i in range(r+2):
            if sr + 1 < r:
                if bd[sr+1][sc] == 0:
                    no += 1
                    bd[sr+1][sc] = no
                    sr += 1
                else : 
>>>>>>> ee8de43198a6a586f4d01d7a0955a17ae6e7fd4c
                    break
            else :
                break
<<<<<<< HEAD
        else :
            break
    if not fin :
        break
    for i in range(c+2):
        if sc - 1 >= 0 :
            if bd[sr][sc-1] == 0:
                no += 1
                if no == point:
                    print(sc, abs(r-sr))
                    fin = False
=======
        for i in range(c+2):
            if sc - 1 >= 0 :
                if bd[sr][sc-1] == 0:
                    no += 1
                    bd[sr][sc-1] = no
                    sc -= 1
                else:
>>>>>>> ee8de43198a6a586f4d01d7a0955a17ae6e7fd4c
                    break
            else:
                break
<<<<<<< HEAD
        else:
            break
if fin :
    print(0)
=======
    for x in range(r):
        for y in range(c):
            if bd[x][y] == point:
                print(y+1, r-x)
>>>>>>> ee8de43198a6a586f4d01d7a0955a17ae6e7fd4c
