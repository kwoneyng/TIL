n,m,k = map(int, input().split()) #여 2 남 1 인턴

while k > 0 :
    a = m*2
    if n % 2 == 1:
        n -= 1
        k -= 1
    elif n - a > 0:
        n -= 1
        k -= 1
    elif m > 1 :
        m -= 1
        k -= 1
    else :
        n -= 1
        k -= 1

if n/m > 2:
    print(m)
else :
    print(n//2)
