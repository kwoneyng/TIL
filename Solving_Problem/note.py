for T in range(10):
    t_no = int(input())
    var_wd = input()
    a = list(map(str, input().split(var_wd)))
    print(f'#{T+1} {len(a)-1}')
