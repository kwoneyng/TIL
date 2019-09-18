n,k = map(int, input().split())
a = [int(input()) for i in range(n)]
rs = 0
for i in range(len(a)-1,-1,-1):
    if k // a[i] > 0:
        rs += k//a[i]
        k %= a[i]
print(rs)