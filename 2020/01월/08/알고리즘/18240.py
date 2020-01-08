def findtree():
    ht = {}
    for i in range(1,n):
        if not ht.get(data[i]):
            ht[data[i]] = [i]
        else:
            ht[data[i]].append(i)


n = int(input())
data = list(map(int,input().split()))
ls = [0]*n
findtree()
maketree()
