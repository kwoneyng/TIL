for i in range(int(input())):
    L, U, X = map(int,input().split())
    result = 0
    if X > U :
        result = -1
    elif X < L :
        result = L - X
    else : 
        result = 0
    print(f'#{i+1} {result}')