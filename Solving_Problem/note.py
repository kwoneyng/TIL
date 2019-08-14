for T in range(1):
    v, e = list(map(int, input().split()))
    ls_e = []
    N = list(map(int, input().split()))
    print(v, e, N)
    al = set(N)
    while len(N) > 0 :
        su = []
        for i in range(2):
            su.append(N.pop(0))
        ls_e.append(su)
    print(f'ls_e={ls_e}')  # 순서쌍
    al = list(al)
    ls = [set() for i in range(len(al))]
    # [[]]*len(al)
    print(ls)  # 뒤에 무엇이 나올지 저장하는 공간
    print(al)  # 포함하고 있는 모든 숫자
    for i in ls_e:
        ls[al.index(i[0])].add(i[1])
    for j in range(1, len(ls)+1):  # 뒤에 순서에 있는거 차근차근 넣어주는 과정

    print(ls)
        
    