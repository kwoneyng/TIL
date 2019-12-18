from collections import deque

n = int(input())
cnt = 0
rs = []
if n % 2 == 1:
    n *= 2
    cnt += 1
    rs.append('[/]')
while n > 2:
    if (n//2) % 2 == 0:
        n //= 2
        cnt += 1
        rs.append('[*]')
    else: 
        n += 2
        cnt += 1
        rs.append('[-]')
        n //= 2
        cnt += 1
        rs.append('[*]')
cnt += 1
rs.append('[+]')
print(cnt)
rs.reverse
print(rs)