def valid():
    for i in range(n-1):
        dep = data[i]
        if counts[dep] + 1 > counts[dep-1] * 2:
            return 0
        counts[data[i]] += 1
    return 1

def maketree():
    numbers = list(range(n+1))
    nxt_no = list(range(1,n+2))
    dep = dgr
    rs = [[0] * counts[i] for i in range(dep+1)]
    start = 1
    while dep >= 0:
        idx = start
        start = nxt_no[idx]

        for i in range(counts[dep]-1):
            rs[dep][i] = idx
            nxt = nxt_no[idx]
            n_nxt = nxt_no[nxt]
            nxt_no[nxt] = nxt_no[n_nxt]
            idx = n_nxt
        
        rs[dep][-1] = idx
        dep -= 1
    
    answer = [str(rs[0][0])] + ['-'] * (n-1)
    for i in range(n-1):
        answer[i+1] = str(rs[data[i]].pop(0))

    print(' '.join(answer))
    return

n = int(input())
data = list(map(int,input().split()))

dgr = max(data)
counts = [1] + [0]*dgr
if valid():
    print(counts)
    maketree()
    
else:
    print(-1)