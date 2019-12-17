def make(i,j):
    if j not in node[i]:
        node[i].append(j)
        indegree[j] += 1

def topologicalSort():
    q = []
    result = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n):
        if not q:
            return [0]
        x = q.pop(0)
        result.append(x)
        for nxt in node[x]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return result

n,m = map(int, input().split())
node = [[] for _  in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    nodes = list(map(int,input().split()))
    for i in range(1,nodes[0]+1):
        for j in range(i+1, nodes[0]+1):
            make(nodes[i], nodes[j])
for i in topologicalSort():
    print(i)