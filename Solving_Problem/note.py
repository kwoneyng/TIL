def fnr(ls):
    


for T in range(2):
    S, N = list(map(int, input().split()))
    ls = list(map(str, input().split()))
    Bl = []
    for i in range(0,len(ls),2):
        su = []
        for j in range(2):
            su.append(ls[i+j])
        Bl.append(su)
    print(Bl)
