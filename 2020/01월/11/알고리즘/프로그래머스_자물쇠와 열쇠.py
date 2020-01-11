near = [[0,1], [1,0]]
def rotate(key):
    temp = [i[:] for i in key]

    for i in range(len(key)):
        for j in range(len(key)):
            key[i][j] = temp[len(key)-j-1][i]
    
    return key

def insert(answer,m,n,bd,cnt,key,x,y):
    if answer == True:
        return
    rs = 0
    for i in range(m):
        for j in range(m):
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
        answer = True
        return True

def solution(key, lock):
    cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                cnt += 1
    n = len(lock)
    m = len(key)
    bd = [[0]*(n+(2*(m-1))) for i in range(n+(2*(m-1)))]
    r1 = [i[:] for i in rotate(key)]
    r2 = [i[:] for i in rotate(key)]
    r3 = [i[:] for i in rotate(key)]
    r4 = [i[:] for i in rotate(key)]
    q = [r1,r2,r3,r4]
    
    answer = False
    for k in q:
        if answer == True:
            break
        for x in range(n+m-2):
            for y in range(n+m-2):
                if insert(answer,m,n,bd,cnt,k,x,y) == True:
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))