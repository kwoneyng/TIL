bd = []
for i in range(100):
    bd.append([0 for i in range(100)])
for j in range(4):
    st_x, st_y, en_x, en_y = list(map(int, input().split()))
    for x in range(st_x, en_x):
        for y in range(st_y, en_y):
            bd[x][y] = 1
area = 0
for i in bd:
    area += i.count(1)
print(area)