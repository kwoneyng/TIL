for T in range(10):
    bd = []
    t_no = int(input())
    count = 0
    for i in range(t_no):
        bd.append(list(map(int, input().split())))  # 판 구성
    bd_ro = list(map(list, zip(*bd)))  # 자성을 편하게 다루기 위해 세로줄을 가로줄로 바꿔줌
    for x in range(len(bd_ro)):  # br의 x번째 열 == br_ro 의 x번째 행
        for y in range(len(bd_ro)):  # br의 x번째 열에서 한칸씩 내려오며 확인 == br_ro의 x번째 행에서 한칸씩 이동하며 확인
            if len(bd_ro[x]) == 0 :
                break
            else :
                if bd_ro[x][0] == 1:  # 교착상태가 생기기 위해선 반드시 1, 2의 순서로 만나야 함(자성 확인) 아닐 경우 삭제
                    if 2 in bd_ro[x]:  # 뒤에 2가 없으면 1이 테이블로 떨어지므로 뒤에 2가 있는지 확인
                        pair = bd_ro[x].index(2)  # 있을 경우 가장 앞에 있는 2의 인덱스 호출
                        del bd_ro[x][0:pair+1]  # 1부터 2까지 모든 수를 제거함
                        count += 1  # 교착상태가 만들어져서 count를 1 올려줌
                    else :
                        break
                else : 
                    del bd_ro[x][0]  # 위의 ==1 에서 1이 아닐경우 삭제
    print(f'#{T+1} {count}')                                
    