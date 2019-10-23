def change(ls, cnt=0):
    rs = int(''.join(ls))
    if rs > mx_cnt[cnt]:
        mx_cnt[cnt] = rs
    else:
        return
    if cnt == count:
        return
    for i in range(ls_len):
        for j in range(i+1, ls_len):
            ls[i], ls[j] = ls[j], ls[i]
            change(ls, cnt+1)
            ls[j], ls[i] = ls[i], ls[j]

for t in range(int(input())):
    data, count = list(input().split())
    count = int(count)
    data = list(data)
    ls_len = len(data)
    mx_cnt = [0]*(count+1) 
    change(data)
    print('#{}'.format(t+1),mx_cnt[-1])