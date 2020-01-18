def rotate(key):
    lis = []
    for i in range(len(key)):
        li = []
        for j in range(len(key)):
            li.append(key[len(key)-j-1][i])
        lis.append(li)
    return lis

def insert(bd,key,lock,cnt,x,y):
    rs = 0
    m = len(key)
    n = len(lock)
    for i in range(len(key)):
        for j in range(len(key)):
            if m-2 < i+x < n+m-1 and m-2 < j+y < n+m-1:
                if bd[i+x][j+y] == 0:
                    if key[i][j] == 1:
                        rs += 1
                        continue
                    else:
                        return 0
                else:
                    if key[i][j] == 0:
                        continue
                    else:
                        return 0
    if rs == cnt:
        return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    near = [[0,1],[1,0]]
    temp = [i[:] for i in key]
    r1 = rotate(key)
    r2 = rotate(r1)
    r3 = rotate(r2)
    q = [key,r1,r2,r3]
    bd = [[0]*(n+(2*(m-1))) for i in range(n+(2*(m-1)))]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bd[i][j] == 0:
                cnt += 1
    for i in range(len(lock)):
        for j in range(len(lock)):
            bd[m+i-1][m+j-1] = lock[i][j]
            
    for k in q:
        for x in range(n+m-2):
            for y in range(n+m-2):
                if insert(bd,key,lock,cnt,x,y) == True:
                    return True
    
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))