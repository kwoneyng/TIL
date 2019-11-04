n = int(input())
a = list(map(int,input().split()))
b,c = map(int, input().split())
man = 0
for i in a:
    if i-b > 0:
        man += (i-b)//c
        if (i-b)%c:
            man += 1
    man += 1
print(man)
