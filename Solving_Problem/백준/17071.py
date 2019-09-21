n, m = map(int, input().split())
Hs0 = [0]*500001
Hs1 = [0]*500001
q = [n]
Hs0[n] = 1
for i in range(100000):
    if i % 2 == 0:
        ls_c = Hs0
        ls_n = Hs1
    else:
        ls_c = Hs1
        ls_n = Hs0
    m+=i
    if m > 500000:
        print(-1)
        break
    if ls_c[m] == 1:
        print(i)
        break
    for j in range(len(q)):
        chk = q.pop(0)
        if chk+1 <= 500000:
            if ls_n[chk+1] == 0:
                ls_n[chk+1] = 1
                q.append(chk+1)
        if chk-1 >= 0:
            if ls_n[chk-1] == 0:
                ls_n[chk-1] = 1
                q.append(chk-1)
        if chk*2 <= 500000 :
            if ls_n[chk*2] == 0:
                ls_n[chk*2] = 1
                q.append(chk*2)