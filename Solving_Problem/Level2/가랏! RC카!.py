def receive(a):
    if len(list(map(int, a.split()))) == 1:
        return [int(a), 0]
    else :
        return list(map(int, a.split()))

for i in range(int(input())):
    speed = 0
    dist = 0
    for j in range(int(input())):
        kind, val = receive(input())
        if kind == 1 :
            speed += val
        elif kind == 2 :
            if speed - val < 0 :
                speed = 0
            else :
                speed -= val
        dist += abs(speed)
    print(f'#{i+1} {dist}')
