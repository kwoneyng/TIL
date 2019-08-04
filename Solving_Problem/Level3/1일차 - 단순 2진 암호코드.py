pw = [(0, '0001101'), (1, '0011001'), (2, '0010011'), (3, '0111101'), (4, '0100011'), (5, '0110001'), (6, '0101111'), (7, '0111011'), (8, '0110111'), (9, '0001011')]
val = [pw[i][1] for i in range(10)]

for T in range(int(input())):
    N, M = list(map(int, input().split()))
    rs = set()
    for i in range(N):
        su_set = []
        st = list(map(int, input()))
        if sum(st) == 0:
            continue
        for j in range(10000):
            if sum(st[:4]) == 0:
                if len(st) > 0:
                    st.pop(0)
            elif ''.join(map(str, st[:7])) in val and ''.join(map(str, st[7:14])) in val:
                for i in pw:
                    if ''.join(map(str, st[:7])) in i:
                        su_set.append(i[0])
                for j in pw:
                    if ''.join(map(str, st[7:14])) in j:
                        su_set.append(j[0])
                del st[:14]
            else :
                if len(st) > 0:
                    st.pop(0)
                else :
                    break
        if len(su_set) > 7 :
            if ((su_set[0] + su_set[2] + su_set[4] + su_set[6])*3 + su_set[1] + su_set[3] + su_set[5] + su_set[7]) % 10 == 0:
                rs.update([sum(su_set)])
            else :
                rs.update([0])
    print('#{0} {1}'.format(T+1, rs.pop()))    
