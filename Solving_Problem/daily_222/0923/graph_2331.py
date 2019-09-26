a, p = list(map(str,input().split()))
d = [0]*1000000
vis = [0]*1000000
d[0] = a
for i in range(1000001):
    if vis[int(d[i])] < 2:
        vis[int(d[i])] += 1
        rs = 0
        for j in d[i]:
            rs += int(j)**int(p)
        d[i+1] = str(rs)
    else:
        print(d.index(d[i]))
        break