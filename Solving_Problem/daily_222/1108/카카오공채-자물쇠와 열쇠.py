def rotate(key):
    nkey = []
    for y in range(len(key)):
        byun = []
        for x in range(len(key)):
            byun.append(key[x][y])
        nkey.append(byun)
    return nkey

def move(key):
    pass


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

for i in key:
    print(i)
key = rotate(key)
for i in key:
    print(i)