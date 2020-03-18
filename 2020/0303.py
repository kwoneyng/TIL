from collections import deque

def solve(son,sonv,vis,start1=0,start2=0):
    global flag
    if flag == 0 :
        if sonv[0] != optimal:
            for i in range(start1, n):
                if flag == 0 and sonv[0] + arr[i] <= optimal and vis[i] == 0:
                    sonv[0] += arr[i]
                    son[0].append(arr[i])
                    vis[i] = 1
                    solve(son,sonv,vis,i+1)
                    vis[i] = 0
                    son[0].pop()
                    sonv[0] -= arr[i]
        elif sonv[1] != optimal:
            for i in range(start2, n):
                if flag == 0 and sonv[1] + arr[i] <= optimal and vis[i] == 0:
                    sonv[1] += arr[i]
                    son[1].append(arr[i])
                    vis[i] = 1
                    solve(son,sonv,vis,start1,i+1)
                    vis[i] = 0
                    son[1].pop()
                    sonv[1] -= arr[i]
        else:
            for i in range(n):
                if vis[i] == 0:
                    son[2].append(arr[i])
            print(f'#{t+1}')
            for i in son:
                print(' '.join(map(str,i)))
            flag = 1
            return

for t in range(int(input())):
    flag = 0
    n = int(input())
    arr = list(map(int,input().split()))
    total = sum(arr)
    optimal = total//3
    son = [[],[],[]]
    sonv = [0,0,0]
    vis = [0]*n
    solve(son, sonv, vis)