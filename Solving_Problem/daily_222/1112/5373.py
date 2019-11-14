def rotate(ls):
    plate, direct = ls
    if plate == 'U':
        i = 0
        if direct == '-':
            um(i)
        else:
            up(i)
    elif plate == 'D':
        i = 1
        if direct == '-':
            dm(i)
        else:
            dp(i)
    elif plate == 'F':
        i = 2
        if direct == '-':
            fm(i)
        else:
            fp(i)
    elif plate == 'B':
        i = 3
        if direct == '-':
            bm(i)
        else:
            bp(i)
    elif plate == 'L':
        i = 4
        if direct == '-':
            lm(i)
        else:
            lp(i)
    elif plate == 'R':
        i = 5
        if direct == '-':
            rm(i)
        else:
            rp(i)

def um(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[2][0][0], cube[2][0][1], cube[2][0][2]] = [cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[5][2][0], cube[5][1][0], cube[5][0][0]] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[3][2][2], cube[3][2][1], cube[3][2][0]] = [cube[3][2][2], cube[3][2][1], cube[3][2][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]]

def up(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[3][2][2], cube[3][2][1], cube[3][2][0]] = [cube[3][2][2], cube[3][2][1], cube[3][2][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[5][2][0], cube[5][1][0], cube[5][0][0]] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]] ,[cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
    [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[2][0][0], cube[2][0][1], cube[2][0][2]] = [cube[2][0][0], cube[2][0][1], cube[2][0][2]] ,[cube[4][0][2], cube[4][1][2], cube[4][2][2]]
    
def dm(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[2][2][2], cube[2][2][1], cube[2][2][0]] = [cube[2][2][2], cube[2][2][1], cube[2][2][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]] 
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[4][2][0], cube[4][1][0], cube[4][0][0]] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]] 
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][0][1], cube[3][0][2]] = [cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]

def dp(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][0][1], cube[3][0][2]] = [cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[4][2][0], cube[4][1][0], cube[4][0][0]] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
    [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[2][2][2], cube[2][2][1], cube[2][2][0]] = [cube[2][2][2], cube[2][2][1], cube[2][2][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]

def fm(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[1][2][2], cube[1][2][1], cube[1][2][0]] = [cube[1][2][2], cube[1][2][1], cube[1][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[5][2][2], cube[5][2][1], cube[5][2][0]] = [cube[5][2][2], cube[5][2][1], cube[5][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[0][2][2], cube[0][2][1], cube[0][2][0]] = [cube[0][2][2], cube[0][2][1], cube[0][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]

def fp(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[0][2][2], cube[0][2][1], cube[0][2][0]] = [cube[0][2][2], cube[0][2][1], cube[0][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[5][2][2], cube[5][2][1], cube[5][2][0]] = [cube[5][2][2], cube[5][2][1], cube[5][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
    [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[1][2][2], cube[1][2][1], cube[1][2][0]] = [cube[1][2][2], cube[1][2][1], cube[1][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]

def bm(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[0][0][0], cube[0][0][1], cube[0][0][2]] = [cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][0][0], cube[5][0][1], cube[5][0][2]] = [cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[1][0][0], cube[1][0][1], cube[1][0][2]] = [cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]

def bp(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[1][0][0], cube[1][0][1], cube[1][0][2]] = [cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][0][0], cube[5][0][1], cube[5][0][2]] = [cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
    [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[0][0][0], cube[0][0][1], cube[0][0][2]] = [cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]

def lm(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[2][2][0], cube[2][1][0], cube[2][0][0]] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[0][2][0], cube[0][1][0], cube[0][0][0]] = [cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[3][2][0], cube[3][1][0], cube[3][0][0]] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]

def lp(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[3][2][0], cube[3][1][0], cube[3][0][0]] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[0][2][0], cube[0][1][0], cube[0][0][0]] = [cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[2][2][0], cube[2][1][0], cube[2][0][0]] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]

def rm(i):
    cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][2][0], cube[1][1][0], cube[1][0][0]] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[3][0][2], cube[3][1][2], cube[3][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]

def rp(i):
    cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[3][0][2], cube[3][1][2], cube[3][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][2][0], cube[1][1][0], cube[1][0][0]] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]

def debug():
    for i in cube:
        for j in i:
            print(j)



for t in range(int(input())):
    cube = [[['w']*3 for i in range(3)], [['y']*3 for i in range(3)], [['r']*3 for i in range(3)], [['o']*3 for i in range(3)], [['g']*3 for i in range(3)], [['b']*3 for i in range(3)]]
    n = int(input())
    data = list(input().split())
    for i in range(n):
        rotate(data[i])
    for i in cube[0]:
        print(''.join(i))
