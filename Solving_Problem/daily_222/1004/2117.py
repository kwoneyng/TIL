def service(x,y,k):
    hm = 0
    i = 0
    for tx in range(x-(k-1),x):
        for ty in range(y-i,y+i+1):
            if 0 <= tx < n and 0 <= ty < n:
                if bd[tx][ty] > 0:
                    hm +=1
        i += 1
    for tx in range(x, x+k):
        for ty in range(y-i,y+i+1):
            if 0 <= tx < n and 0 <= ty < n:
                if bd[tx][ty] > 0:
                    hm += 1
        i-= 1
    return hm

for t in range(int(input())):
    n,m = map(int,input().split())
    bd = [list(map(int,input().split())) for i in range(n)]
    # 운영비용 = k*k+(k-1)*(k-1)
    mx_hm = 0
    for x in range(n):
        for y in range(n):
            for k in range(n+2):
                rs = service(x,y,k)
                if rs*m - ((k*k)+((k-1)*(k-1))) >= 0:
                    if mx_hm < rs:
                        mx_hm = rs
    print('#{}'.format(t+1), mx_hm)