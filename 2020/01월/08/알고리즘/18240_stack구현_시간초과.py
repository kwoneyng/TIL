from collections import deque

def findtree():
    ht = {}
    can = [0]*(n+1)
    can[1] = 2
    for i in range(1,n):
        if can[data[i-1]] > 0:
            can[data[i-1]] -= 1
            can[data[i-1]+1] += 2
            if not ht.get(data[i-1]):
                ht[data[i-1]] = deque([i])
            else:
                ht[data[i-1]].append(i)
        else:
            return 0
    return ht

def maketree(ht,cur):
    stack = deque([[0,0]])
    s = 1
    dgr = max(ht)
    while stack:
        x, c = stack.pop()
        if c == 1:
            if len(ht[x]) > 0:
                cur[ht[x].popleft()] = str(s)
                s += 1
            stack.append([x+1,0])
        else:
            if x == dgr:
                if len(ht[x]) > 0:
                    cur[ht[x].popleft()] = str(s)
                    s += 1
            else:
                stack.append([x,1])
                stack.append([x+1,0])


n = int(input())
data = list(map(int,input().split()))
ls = [0]*n
ht = findtree()
if ht == 0:
    print(-1)
else:
    ht[0] = deque([0])
    cur = [0]*(n)
    # print(ht)
    maketree(ht,cur)
    print(' '.join(cur))