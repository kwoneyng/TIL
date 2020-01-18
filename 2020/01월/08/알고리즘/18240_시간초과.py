# def go(vis, can):
#     global rs
#     for i in data:
#         if vis[i] > 0:
#             vis[i] -= 1
#         else: 
#             return

# def degree(n):
#     for i in range(n):
#         if 2**i <= n+1 < 2**(i+1):
#             return i+1
# def set_su(dgr):
#     for i in range(dgr):
#         std = 2**(dgr-i-1)
#         term = 2**(dgr-i)
#         for j in range(len(su[i])):
#             su[i][j] = std + term*j


# dgr = degree(n)
# print(dgr)
# stdd = n**(dgr-1)
# rs = -1
# su = []
# for i in range(dgr):
#     su.append([0]*(2**i))
# set_su(dgr)
# print(su)

def findtree():
    global rs
    stdd = 2**mdgr
    ls = [str(stdd)]
    for i in range(len(data)):
        term = 2**(mdgr+1-data[i])
        if can[data[i]] > 0:
            can[data[i]] -= 1
            can[data[i]+1] += 2
            ls.append(str(2**(mdgr-data[i])+cur[data[i]]*term))
            cur[data[i]] += 1
        else:
            return
    rs = ls
    return

n = int(input())
data = list(map(int,input().split()))
mdgr = max(data)
can = [0]*(mdgr+2)
can[1] = 2
dgr = [[] for i in range(mdgr+2)]
rs = -1
cur = [0]*(mdgr+2)

findtree()
if rs == -1:
    print(rs)
else:
    print(' '.join(rs))