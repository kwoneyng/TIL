n = int(input())
bd = [[0]*30 for i in range(30)]
pick = []
pick_set = []
bd = [[0]*30 for i in range(30)]
for i in range(n//5+1):
    pick.extend(list(map(int, input().split())))
for i in range(len(pick)//2):
    pick_set.append([pick[i*2+1], pick[i*2]])

print(pick_set)

for i in range(len(pick_set)-1):
    if i%2 == 0:
        ul = [pick_set[i][1], pick_set[i+1][1]]
        for y in range(min(ul), max(ul)+1):
            bd[pick_set[i][0]][y] = 1
    else :
        ul = [pick_set[i][0], pick_set[i+1][0]]
        for x in range(min(ul), max(ul)+1):
            bd[x][pick_set[i][1]] = 1
ul = [pick_set[0][0],pick_set[-1][0]]
for x in range(min(ul), max(ul)+1):
    bd[x][pick_set[0][1]] = 1
        
for i in bd:
    print(i)