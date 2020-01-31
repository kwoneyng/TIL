from collections import deque

n = int(input())
cnt = 0
rs = ''
if n % 2 == 1:
    n *= 2
    cnt += 1
    rs += ' ]/['
while n > 2:
    if (n//2) % 2 == 0:
        n //= 2
        cnt += 1
        rs += ' ]*['
    else: 
        n += 2
        cnt += 1
        rs += ' ]-['
        n //= 2
        cnt += 1
        rs += ' ]*['
cnt += 1
rs += ' ]+['
print(cnt)
print(rs[::-1])