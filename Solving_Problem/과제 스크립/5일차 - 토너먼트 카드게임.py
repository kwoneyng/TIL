def div(ls):
    while True:
        if len(ls) == 1:
            return ls[0]
        if len(ls) == 2:
            if win(ls[0], ls[1]) == 1:
                return ls[0]
            else :
                return ls[1]
        else :
            a = div(ls[:(len(ls)+1)//2])
            del ls[:(len(ls)+1)//2]
            b = div(ls)
            del ls[:]
            ls.append(a)
            ls.append(b)

def win(x, y):
    if x[1] == 1 :
        if y[1] != 2 :
            return 1
        else :
            return 0
    elif x[1] == 2 :
        if y[1] != 3 :
            return 1
        else :
            return 0
    elif x[1] == 3 :
        if y[1] != 1 :
            return 1
        else :
            return 0


for T in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    su = []
    i = 0
    print('#{} '.format(T+1), end='')
    while i < n:
        su.append([i+1, s[i]])
        i += 1
    print(div(su)[0])