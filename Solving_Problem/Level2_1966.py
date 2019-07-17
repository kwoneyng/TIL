for i in range(int(input())):
    N = int(input())
    t_no = list(map(int, input().split()))
    print(f'#{i+1}', end = ' ')
    for j in sorted(t_no) :
        print(f'{j}', end = ' ')
    print('')