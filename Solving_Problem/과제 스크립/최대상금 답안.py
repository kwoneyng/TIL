def find(lst, idx, c):
    global max
    if c == 0:
        t = int(''.join(lst))
        if max < t:
            max = t
        return l = len(lst)
    for i in range(idx, l-1):
        for j in range(i+1, l):
            if lst[i] <= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                find(lst, i, c-1)
                lst[i], lst[j] = lst[j], lst[i]
 
T = int(input())
for tc in range(1, T+1):
    N, C = map(int, input().split())
    Lst = list(str(N))
    max = 0
    find(Lst, 0, C)
    print("#{} {}".format(tc, max))