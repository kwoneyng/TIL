end_point = [1 for i in range(150)]
for i in range(1,150):
    for j in range(i,150):
        end_point[j] += i+1
def find_floor(x):
    for i in range(150):
        if x <= end_point[i]:
            return i

def position(af,bf,ap,bp):
    if af == 0:
        ap = 0
    if ap < bp:
        if bp-ap > bf-af:
            return bp-ap - (bf-af)
        else: return 0
    else:
        return ap-bp



for t in range(int(input())):
    a,b = list(map(int,input().split()))
    if a > b :
        a,b = b,a
    af = find_floor(a)
    bf = find_floor(b)
    ap = a - end_point[af-1]
    bp = b - end_point[bf-1]
    df = abs(af-bf)
    dr = position(af,bf,ap,bp)
    rs = df + dr
    # print(df, dr)
    print(f'#{t+1} {rs}')