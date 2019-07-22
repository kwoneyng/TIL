for T in range(int(input())):
    t_cs = int(input())
    st = input()
    st_qi = []
    st_qie = []
    st_q = st.split('?')
    al_cl = []
    for i in st_q:
        st_qi += i.split('!')
    for j in st_qi:
        st_qie += j.split('.')
    li_com = st_qie[0:t_cs]
    for k in li_com:
        a = list(map(str, k.split()))
        al_cl.append(a)
    cnt_set = []
    print(f'#{T+1} ', end='')
    for x in al_cl :
        count = 0
        for y in x :
            if y.isalpha():
                if y[0].isupper():
                    if len(y) == 1:
                        count += 1
                    elif y[1:].islower():
                        count += 1
        print(f'{count}', end=' ')
    print('')
