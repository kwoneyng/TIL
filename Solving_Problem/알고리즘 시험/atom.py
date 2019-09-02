for T in range(int(input())):
    n = int(input())
    x = [[] for i in range(2001)]
    y = [[] for i in range(2001)]
    energy = 0
    calc_q = []
    for i in range(n):
        s = list(map(int, input().split()))
        if s[2]//2 == 0 :
            y[s[0]+1000].append([s[1], s[2], s[3]])
        else :
            x[s[1]+1000].append([s[0], s[2], s[3]])
    for i in range(len(x)):
        x[i] = sorted(x[i], key=lambda x:x[0])
    while True :
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j][1] == 2:
                    if -1000 <= x[i][j][0] -1 :
                        x[i][j][0] -= 1
                    else : 
                        x[i].pop(j)
                else :
                    if x[i][j][0] + 1 <= 1000 :
                        x[i][j][0] += 1
                    else :
                        x[i].pop(j)
        for i in range(len(y)):
            for j in range(len(y[i])):
                if y[i][j][1] == 0:
                    if y[i][j][0] + 1 <= 1000:
                        y[i][j][0] += 1
                    else :
                        y[i].pop(j)
                else :
                    if -1000 <= y[i][j][0] - 1:
                        y[i][j][0] -= 1
                    else :
                        y[i].pop(j)
        for i in range(2001):
            if [x[i], i-1000] == [i-1000, y[i]]


