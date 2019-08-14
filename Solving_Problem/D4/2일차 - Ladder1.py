def go(ls, x, y, look=2):
    if x == 0:
        return 1, y
    top = [[0, 1], [0, -1], [-1, 0]]
    left = [[0, -1], [-1, 0]]
    right = [[0, 1], [-1, 0]]

    if look == 2:
        fr = 0
        for a, b in top:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '1':
                    A = go(ls, x+a, y+b,fr)
                    if A[0] == 1:
                        return 1, A[1]
            fr += 1
        return 0, 0
    if look == 1:
        fr = 1
        for a, b in left:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '1':
                    A = go(ls, x+a, y+b,fr)
                    if A[0] == 1:
                        return 1, A[1]
            fr += 1
        return 0, 0
    if look == 0:
        fr = 0
        for a, b in right:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '1':
                    A = go(ls, x+a, y+b,fr)
                    if A[0] == 1:
                        return 1, A[1]
            fr += 2
        return 0, 0
    return 0, 0

for T in range(10):
    ladder = []
    n = int(input())
    for i in range(100):
        ladder.append(input().split())
    start = []
    for j in range(100):
        if ladder[99][j] == '2':
            start = j
    print(f'#{T+1} ',end='')
    print(go(ladder, 99, start)[1])
