def clean(x,y):
    bd[x,y] = 2


n,m = map(int, input().split())
x,y,d = map(int,input().split())
x-=1
y-=1
bd=[list(map(int,input().split())) for i in range(n)]
