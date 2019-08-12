def search(st1,st2):
    st_set = set()
    for i in st1:
        st_set.update(i)
    index = [0]*len(st_set)
    cnt = 0
    for j in st_set:
        for k in st2:
            if j == k:
                index[cnt] += 1
        cnt += 1
    return index

def mmx(ls):
    mx = 0
    for i in ls:
        if mx < i :
            mx = i
    return mx

for T in range(int(input())):
    st1 = input()
    st2 = input()
    print(f'#{T+1} ',end='')
    print(mmx(search(st1, st2)))
