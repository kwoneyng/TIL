near = [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]

def spring():
    for i in range(len(q)-1,-1,-1):
        x,y,z = q.pop(i)
        if bd[x][y] >= z:
            bd[x][y] -= z
            q.append([x,y,z+1])
        else:
            death.append([x,y,z])


def summer():
    for i in range(len(death)-1,-1,-1):
        x,y,z = death.pop(i)
        bd[x][y] += z//2


def fall():
    for i in range(len(q)):
        x,y,z = q[i]
        if z % 5 == 0:
            for dx, dy in near:
                xi = x+dx
                yi = y+dy
                if 0 <= xi < n and 0 <= yi < n:
                    q.append([xi, yi, 1])


def winter():
    for x in range(n):
        for y in range(n):
            bd[x][y] += A[x][y]



n,m,k = map(int,input().split())
bd = [[5]*n for i in range(n)]
A = [list(map(int,input().split())) for i in range(n)]
q = []
death = []
q.sort(key=lambda x: x[2])
for i in range(m):
    x,y,z = map(int,input().split())
    q.append([x-1,y-1,z])
for tk in range(k):
    spring()
    summer()
    fall()
    winter()
    q.sort(key=lambda x: x[2])
print(len(q))

# 5 2 7
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3
# ans 71