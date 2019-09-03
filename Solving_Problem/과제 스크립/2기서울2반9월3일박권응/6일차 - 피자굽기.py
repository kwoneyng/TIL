for T in range(int(input())):
    n, m = map(int, input().split())
    ci_ls = list(map(int, input().split()))
    queue = []
    idx = 0
    while len(queue) < n:
        idx += 1
        queue.append([idx, ci_ls.pop(0)])
    while queue:
        a = queue.pop(0)
        nxt_chz = a[1]//2
        if nxt_chz == 0:
            if ci_ls:
                idx += 1
                queue.append([idx, ci_ls.pop(0)])
        else :
            queue.append([a[0], nxt_chz])
    print('#{}'.format(T+1),a[0])
