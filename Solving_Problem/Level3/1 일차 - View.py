for T in range(10):
    N = int(input())
    a = list(map(int, input().split()))
    m_v = 0
    b_s = []
    for i in range(2, N-2):
        if a[i] > max(a[i-2:i]) :
            m_v = a[i] - max(a[i-2:i])
            if a[i] > max(a[i+1:i+3]):
                if m_v > a[i]-max(a[i+1:i+3]) :
                    m_v = a[i] - max(a[i+1:i+3])
                b_s.append(m_v)
    print(f'#{T+1} {sum(b_s)}')