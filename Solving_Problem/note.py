def move(ls, start, cnt=0):
        for i in range(len(ls)):
            if ls[start][1] == ls[i][0]:
                if move(ls, ls[i] cnt+1) == 1:
                    return 1
        return 1

for T in range(1):
    v, e = map(int, input().split())
    st = input().split()
    tar = []
    while len(st) > 0: 
        su = []
        for i in range(2):
            su.append(st.pop(0))
        tar.append(su)
    print(tar)