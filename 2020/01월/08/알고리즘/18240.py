def findtree():
    ht = {}
    for i in range(1,n):
        if not ht.get(data[i-1]):
            ht[data[i-1]] = [i]
        else:
            ht[data[i-1]].append(i)
    return ht

n = int(input())
data = list(map(int,input().split()))
ls = [0]*n
ht = findtree()
# maketree()
print(ht)