import time

T = int(input())
for t in range(1, T+1):
    # K = 최대이동거리 / N = 총 정류장 수 / M = 충전기가 있는 정류장 번호
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    M_list.append(N)
    state = 0
    count = 0
    while state < N:  # N에 도착하거나 N보다 커지면 멈춤
        time.sleep(0.5)
        print(state)
        state = state + K
        print('------------')
        print(state)
        if state in M_list:
            count += 1
        else:
            while state not in M_list:
                state -= 1  # 충전소를 만나면 다시 위쪽 while로 돌아가야함
                if K == 0:
                    count = 0
                    break
    print('#{0} {1}'.format(t, count))