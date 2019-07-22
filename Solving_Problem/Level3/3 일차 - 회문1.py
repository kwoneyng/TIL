# 3일차 - 회문 1
import math

for i in range(10):
    t_no = int(input())
    t_var = math.floor(t_no/2)  # 회문의 길이를 반으로 나누어 앞뒤의 값이 같은지 확인하기 위해
    board = []
    chk = 0
    for j in range(8):
        board.append([i for i in input()])  # 판 생성
    for k in range(8):
        pal = board[k]  # k번째 행
        for z in range(9-t_no):  # k번째 행 내에서 한칸씩 이동하면서 확인
            ck_s = 0
            if t_no % 2 == 1:  # 회문 길이가 홀수일 때
                for t in range(t_var) :  
                    if pal[z+t]==pal[z-t+t_no-1]:  # abcde -> (a,e) (b,d) 비교
                        ck_s += 1
            else :
                for t in range(t_var) :
                    if pal[z+t]==pal[z-t+t_no-1]:  # abcd -> (a, d) (b, c) 비교
                        ck_s += 1
            if ck_s == t_var:
                chk += 1
    # board_z = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7]))
    board_z = list(map(list, zip(*board)))  # 세로줄을 뽑아와서 판 재구현
    for a in range(8):
        pal_z = board_z[a]
        for b in range(9-t_no):
            ckz_s = 0
            if t_no % 2 == 1:
                for c in range(t_var) :
                    if pal_z[b+c]==pal_z[b-c+t_no-1]:
                        ckz_s += 1
            else :
                for c in range(t_var) :
                    if pal_z[b+c]==pal_z[b-c+t_no-1]:
                        ckz_s += 1
            if ckz_s == t_var:
                chk += 1
    
    
    print(f'#{i+1} {chk}')
