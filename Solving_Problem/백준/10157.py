c, r = map(int, input().split())
point = int(input())
bd = []
for row in range(r):
    bd.append([0 for i in range(c)])
no = 0
sr, sc = [r, 0]
fin = True
while fin:
    for i in range(r+2):
        if sr - 1 >= 0 :
            if bd[sr-1][sc] == 0:
                no += 1
                if no == point:
                    print(sc+1, r-sr-1)
                    fin = False
                    break
                bd[sr-1][sc] = no
                sr -= 1
            else :
                break
        else :
            break
    if not fin :
        break
    for i in range(c+2):
        if sc + 1 < c:
            if bd[sr][sc+1] == 0:
                no += 1
                if no == point:
                    print(sc+2, r-sr)
                    fin = False
                    break
                bd[sr][sc+1] = no
                sc += 1
            else:
                break
        else :
            break
    if not fin :
        break
    for i in range(r+2):
        if sr + 1 < r:
            if bd[sr+1][sc] == 0:
                no += 1
                if no == point:
                    print(sc+1, r-sr+1)
                    fin = False
                    break
                bd[sr+1][sc] = no
                sr += 1
            else : 
                break
        else :
            break
    if not fin :
        break
    for i in range(c+2):
        if sc - 1 >= 0 :
            if bd[sr][sc-1] == 0:
                no += 1
                if no == point:
                    print(sc, r-sr)
                    fin = False
                    break
                bd[sr][sc-1] = no
                sc -= 1
            else:
                break
        else:
            break