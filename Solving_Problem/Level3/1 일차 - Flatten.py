for T in range(10):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N):
        a[a.index(max(a))] -= 1
        a[a.index(min(a))] += 1
    print(f"#{T+1} {max(a) - min(a)}")