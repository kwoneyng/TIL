bd=[list(map(int, input().split())) for i in range(10)]
p = [5,4,3,2,1]
p_use = [5,5,5,5,5]
q = []
cnt = 0
for x in range(10):
    for y in range(10):
        if bd[x][y] == 1:
            q.append([x,y])

for i in range(5):
    for j in range(len(q)):
        x,y = q[j]
        if bd[x][y] == 0:
            continue
        if i < 4:
            if p_use[i] == 0:
                use = 0
                break
        use = 1
        for xi in range(x,x+p[i]):
            if not use:
                break
            for yi in range(y,y+p[i]):
                if 0 <= x+p[i]-1 < 10 and 0 <= y+p[i]-1 < 10:
                    if bd[xi][yi] == 0:
                        use = 0
                        break
                else :
                    use = 0
                    break
        if use:
            cnt += 1
            p_use[i] -=1
            for xi in range(x,x+p[i]):
                for yi in range(y,y+p[i]):
                    bd[xi][yi] = 0
if p_use[-1] >= 0:
    print(cnt)
else:
    print(-1)
