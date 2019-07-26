for T in range(10):
    st_i = int(input())
    n = list(map(int, input().split()))
    la_i = 2
    i = 0
    print(f'#{T+1}', end=' ')
    while la_i > 1 :
       for j in range(5):
           i += 1
           la_i = n.pop(0) - i
           if la_i <= 0 :
              la_i = 0
              n.append(la_i)
              break
           else :
              n.append(la_i)
       i = 0
    print(' '.join(map(str,n)))
