def m_x(ls):
    mx = ls[0]
    for i in ls:
        if mx < i:
            mx = i
    return mx

def m_n(ls):
    mn = ls[0]
    for i in ls :
        if mn > i:
            mn = i
    return mn
    
def i_p(ls,x):
    idx = 0
    for i in ls:
        if x == i:
            rs = i
            del ls[idx]
            break
        else :
            idx += 1
    return rs

for T in range(int(input())):
    N = int(input())
    ls = list(map(int, input().split()))
    n_ls = []
    rs = ""
    for i in range(len(ls)):
        if len(ls) > 1:
            n_ls.append(i_p(ls, m_x(ls)))
            n_ls.append(i_p(ls, m_n(ls)))
        elif len(ls) == 1 :
            n_ls.append(ls[0])
            break
        else :
            break
    # print(n_ls)
    for i in n_ls[:10]:
        rs += str(i) + ' '
    print(f'#{T+1}', end=' ')
    print(rs)

