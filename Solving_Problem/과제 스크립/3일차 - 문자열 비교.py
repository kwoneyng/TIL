def lssl(str, first, last, reverse=False):
    rs = ''
    for i in range(first,last):
        rs += str[i]
    return rs


for T in range(int(input())):
    N = input()
    S = input()
    rs = 0
    for i in range(len(S)-len(N)+1):
        A = lssl(S, i, len(N)+i)
        if A == N :
            rs = 1
    print(f'#{T+1} ',end='')
    print(rs)
