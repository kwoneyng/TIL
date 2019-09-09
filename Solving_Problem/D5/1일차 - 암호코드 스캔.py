for T in range(int(input())):
    n, m = map(int, input().split())
    code_set = []
    for i in range(n):
        a = list(input())
        su = ''
        for i in a:
            if i != '0':
                su = su + i
        if len(su) == 