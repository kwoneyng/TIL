for i in range(int(input())):
    N = int(input())
    flr = ''
    count = 0
    for j in range(N):
        c, k = list(input().split())
        flr += c*int(k)
        count += 1
    result = ''
    print(f'#{i+1}')
    for k in flr:
        if len(result) == 10 :
            print(result)
            result = ''
            result += k
        else :
            result += k
    print(result)
