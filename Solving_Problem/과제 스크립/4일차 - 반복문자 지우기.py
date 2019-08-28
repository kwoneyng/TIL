for T in range(int(input())):
    s = list(input())
    while True :
        stop = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                del s[i:i+2]
                stop = 1
                break
        if stop == 0:
            break
    print(f'#{T+1} ',end='')
    print(len(s))
