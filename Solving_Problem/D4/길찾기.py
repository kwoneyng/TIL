import time

def fnr(ls, end=0):
    if end == 99:
        return 1
    #보니까 0으로 시작하는게 1개가 아님
    for i in range(1, len(ls)):  # ls의 첫번째 순서쌍을 기준으로 연결되는 모든 순서쌍을 찾는 과정
        if ls[0][1] == ls[i][0]:
            if fnr(ls[i:], ls[i][1]) == 1:  # 출발점이 가장 작은 순서대로 정렬하였으므로 리스트를 다시
                return 1                    # 잘라와서 같은 방식으로 연결되는 순서쌍을 찾는다.
    return 0

for T in range(10):
    S, N = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    Bl = []
    for i in range(0,len(ls),2):  # 순서쌍 나눠주기
        su = []
        for j in range(2):
            su.append(ls[i+j])
        Bl.append(su)
    Bl = sorted(Bl,key = lambda x:x[0])  # 시작하는 수가 작은순으로 정렬
    cnt = 0
    start = []
    for j in Bl:  # 0부터 출발하므로 출발점이 0인 지점을 찾아 추가한다.
        if 0 in j:
            start.append(j)
            cnt += 1  # 시작점을 제외한 리스트를 만들기 위해 cnt를 세어준다.
    del Bl[:cnt]
    rs = []
    for k in start:  # 0부터 출발
        sl = [k] + Bl
        rs.append(fnr(sl))  # 0부터 출발하는 모든 경우를 탐색하고 결과를 rs에 저장한다.
    if 1 in rs:  # rs 리스트에 1이 들어있을 경우 99까지 가는 길이 있다는 뜻이므로 결과값 1을 반환한다.
        rs = 1
    else :
        rs = 0
    print(f'#{T+1} ',end='')
    print(rs)
