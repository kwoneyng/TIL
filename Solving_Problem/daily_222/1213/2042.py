import sys
input = sys.stdin.readline

def make_tree(degree):
    if degree == 0:
        return
    for i in range(2**degree,2**degree*2,2):
        numbers[i//2] = numbers[i] + numbers[i+1]
    make_tree(degree-1)


def calc(data):
    a,b,c = data
    if a == 1:
        numbers[stdd+b-1], temp = c, numbers[stdd+b-1]
        for i in range(1,degree):
            numbers[(stdd+b-1)//(2**i)] += (c-temp)
    elif a == 2:
        dsum(b+stdd-1,c+stdd-1)

def dsum(l, r, rs=0):
    if l > r:
        print(rs)
        return
    if l % 2 == 1:
        dsum(l+1, r, rs+numbers[l])
    elif r % 2 == 0:
        dsum(l, r-1, rs+numbers[r])
    else:
        dsum(l//2, r//2, rs)


n,m,k = map(int,input().split()) # n 수의 개수 m 변경 횟수 k 구간합 구하는 횟수
for i in range(20):
    if 2**(i) <= n < 2**(i+1):
        stdd = 2**(i+1)
        degree = (i+1)
        break
numbers = [0] * (stdd)*2
for i in range(n):
    numbers[stdd + i] = int(input())

for i in range(stdd,stdd*2,2):
    numbers[i//2] = numbers[i] + numbers[i+1]
make_tree(degree)

for i in range(m+k):
    calc(map(int,input().split()))

