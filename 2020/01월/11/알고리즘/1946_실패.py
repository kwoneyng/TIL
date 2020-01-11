for t in range(int(input())):
    n = int(input())
    st = 0
    mt = 0
    sc = 0
    mc = 0
    s1, m1 = map(int,input().split())
    s2, m2 = map(int,input().split())

    if s1 > s2 and m1 < m2:
        mt = [s1, m1]
        st = [s2, m2]
        sc += 1
        mc += 1
    elif s1 < s2 and m1 > m2:
        st = [s1,m1]
        mt = [s2,m2]
        sc += 1
        mc += 1
    elif s1 > s2 and m1 > m2:
        st = [s2,m2]
        mt = [s2,m2]
        if s2 > m2:
            mc += 1
        else:
            sc += 1
    elif s1 < s2 and m1 < m2:
        st = [s1,m1]
        mt = [s1,m1]
        if s1 > m1:
            mc += 1
        else:   
            sc += 1


    for i in range(n-2):
        s, m = map(int,input().split())
        ss, sm = st
        ms, mm = mt

        if s > m:
            if mm > m:
                mt = [s,m]
                if ms > s:
                    mc = 1
                else:
                    sc += 1
            elif ms > s:
                sc += 1
        elif s < m:
            if ss > s:
                st = [s,m]
                if sm > m:
                    sc = 1
                else:
                    mc += 1
            elif sm > m:
                mc += 1
        else:
            if ss > s and mm > m:
                sc = 1
                mc = 0
            elif ss > s:
                st = [s,m]
                if sm > m:
                    sc = 1
                else:
                    st[1] = m
                    mc += 1
            elif sm > m:
                mc += 1
            elif mm > m:
                mt = [s,m]
                if ms > s:
                    mc = 1
                else:
                    mt[0] = s
                    sc += 1
            elif ms > s:
                sc += 1
                mt[0] = s
    print(sc+mc)
    
