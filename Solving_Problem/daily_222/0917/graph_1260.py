n, m, v = list(map(int, input().split()))
ln_st = [list(map(int,input().split())) for i in range(m)]
gp = [[] for i in range(1001)]
gp_q = []
for i in ln_st:
    gp[i[0]].append(i[1])
    gp[i[1]].append(i[0])
    if i[0] not in gp_q:
        gp_q.append(i[0])
    if i[1] not in gp_q:
        gp_q.append(i[1])
for i in gp_q:
    gp[i].sort(reverse=True)

stack = [v]
queue = [v]
st_vis = [v]
q_vis = [v]

while stack:
    chk = stack.pop()
    if chk not in st_vis:
        st_vis.append(chk)
    for i in gp[chk]:
        if i not in st_vis:
            stack.append(i)
print(' '.join(map(str,st_vis)))

for i in gp_q:
    gp[i].sort()

while queue:
    chk = queue.pop(0)
    if chk not in q_vis:
        q_vis.append(chk)
    for i in gp[chk]:
        if i not in q_vis:
            queue.append(i)
print(' '.join(map(str, q_vis)))
