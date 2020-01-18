def simul():
    day = 1
    while True:
        if not ori:
            break
        if not yookri:
            break

        for i in range(len(ori)):
            x = ori.pop(0)
            for nxt in [x-(2**(day-1)), x+(2**(day-1))]:
                if 0 < nxt < n+1:
                    if road[nxt] == day+1:
                        continue
                    ori.append(nxt)
                    road[nxt] = day
        for i in range(len(yookri)):
            x = yookri.pop(0)
            for nxt in [x-(2**day), x+(2**day)]:
                if 0 < nxt < n+1:
                    if road[nxt] == day:
                        print(road[nxt])
                        return
                    else:
                        if nxt not in yookri:
                            yookri.append(nxt)
        day += 1
    print(-1)

n,a,b = map(int, input().split())
road = [-1]*(n+1)
if a % 2 == b % 2:
    ori = [a]
    yookri = [b]
    road[a] = 0
    if road[b] == 0:
        print(0)
    else:
        road[b] = 0
        simul()
    pass
else:
    print(-1)
