era = [1]*100001
era[0] = 0
era[1] = 0 
sosu = []
for i in range(100001):
    if era[i] == 1:
        sosu.append(i)
        for n in range(2,100001):
            if i*n > 100000:
                break
            else:
                era[i*n] = 0

# print(sosu)
tocnt = 0

a,b = map(int,input().split())
for i in range(a,b+1):
    temp = i
    cnt = 0
    while temp > 1:
        for j in sosu:
            if temp % j == 0:
                temp //= j
                cnt += 1
                break
    if cnt in sosu:
        tocnt += 1
print(tocnt)