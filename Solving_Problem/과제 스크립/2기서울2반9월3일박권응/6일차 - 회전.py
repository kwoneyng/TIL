for T in range(int(input())):
    n, m = map(int, input().split())
    n_ls = list(map(int, input().split()))
    queue = [i for i in n_ls]
    for i in range(m):
        queue.append(queue.pop(0))
    print('#{} '.format(T+1),end='')
    print(queue[0])