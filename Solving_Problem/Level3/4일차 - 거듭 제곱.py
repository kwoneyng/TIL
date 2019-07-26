def multi(N, M):
    if M == 0:
        return 1
    return multi(N, M-1)*N

for T in range(10):
    A = int(input())
    N, M = list(map(int, input().split()))
    print(f'#{T+1} {multi(N, M)}')