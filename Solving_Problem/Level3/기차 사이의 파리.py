import math

for T in range(int(input())):
    D, A, B, F = list(map(int, input().split()))  # 받은 변수 집어넣기
    t = 0
    ro = 0
    FD = 0
    for i in range(1000):  # while문을 썼을 때 시간 초과가 나서 값을 도출하기에 충분한 숫자로 for문 설정
        if math.isclose(D,0):  # 기차 사이 거리가 0에 가까워 졌을때 for문 탈출
            break
        else :    
            if ro == 0 :  # 파리가 B기차를 향해 갈 때
                t = D/(B+F)
                D = D - (A+B)*t
                ro = 1
                FD = FD + F*t

            if ro == 1 :  # 파리가 A기차를 향해 갈 때
                t = D/(A+F)
                D = D - (A+B)*t
                ro = 0
                FD = FD + F*t
    print(f'#{T+1} {round(FD,6)}')
