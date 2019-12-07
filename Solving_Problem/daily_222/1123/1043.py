def lets_party(known, party,cnt=0, cur=0):
    global rs
    if cnt == m:
        rs = max(cur,rs)
        return
    real = 0
    unreal = 0
    for i in party[cnt]:
        if known[i] > 0:
            real = 1
            break
    for i in party[cnt]:
        if known[i] < 0:
            unreal = 1
            break
    if real == 1 and unreal == 1:
        return
    elif real == 1:
        for i in party[cnt]:
            known[i] += 1
        lets_party(known, party, cnt+1, cur)
        for i in party[cnt]:
            known[i] -= 1

    elif unreal == 1:
        for i in party[cnt]:
            known[i] -= 1
        lets_party(known,party,cnt+1,cur+1)
        for i in party[cnt]:
            known[i] += 1

    elif unreal == real == 0:
        for i in party[cnt]:
            known[i] += 1
        lets_party(known, party, cnt+1, cur)
        for i in party[cnt]:
            known[i] -= 1
        for i in party[cnt]:
            known[i] -= 1
        lets_party(known,party,cnt+1,cur+1)
        for i in party[cnt]:
            known[i] += 1


n,m = map(int, input().split())
data = list(map(int,input().split()))
data.pop(0)
known = [0]*(n+1)
for i in data:
    known[i] = 1
party = [[] for i in range(m)]
for i in range(m):
    apd = list(map(int,input().split()))
    apd.pop(0)
    party[i].extend(apd)
rs = 0
lets_party(known, party)
print(rs)