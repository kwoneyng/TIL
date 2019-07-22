def receive(a):
    if len(list(map(int, a.split()))) == 1:  # 이날 함수를 배웠나 봅니다. 굳이 만들어놨네요
        return [int(a), 0]
    else :
        return list(map(int, a.split()))  # command가 0일 때 메모리 에러가 발생해서 뒤에 0을 붙여주는 과정입니다.

for i in range(int(input())):
    speed = 0
    dist = 0
    for j in range(int(input())):  # 정해진 횟수만큼 command를 받습니다.
        kind, val = receive(input())  # kind, val 은 각각 command, 입력값을 넣어줬습니다.
        if kind == 1 :  # 1일경우 speed를 val 올려줍니다.
            speed += val
        elif kind == 2 :  # 2일경우 speed를 val 만큼 내려줍니다.
            if speed - val < 0 :
                speed = 0
            else :
                speed -= val
        dist += abs(speed)  # 매 command를 받을 때마다 1초씩 소요됨으로 이동거리는 현재 속도와 같습니다.
                            # 이동거리이므로 방향은 신경쓰지 않기때문에 abs()함수를 통해 절댓값을 씌워줬습니다.
    print(f'#{i+1} {dist}')
