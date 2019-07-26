import operator

test_num = int(input())
for i in range(test_num):
    a = list(map(int, input().split()))
    pp = a[0]
    which = a[1]  # 이때는 여러 변수를 한번에 정하는 법을 몰랐나 봅니다. pp와 which에 사람 수와 대상을 지정했습니다.
    score_set = []
    dic_stu = {}
    dic_rank = []
    result = ''
    for j in range(pp):
        score_set = list(map(int, input().split()))
        dic_stu[j] = round(0.35*score_set[0]+0.45*score_set[1]+0.2*score_set[2],2)  #가중 평균을 표현하고 dict로 정리했습니다.
    sorted_dic = sorted(dic_stu.items(), key=operator.itemgetter(1),reverse=True)  # 점수를 기준으로 정렬을 실행하고 내림차순으로 바꿔줬습니다.
    for j in range(len(sorted_dic)):  # 학점을 10%씩 끊어서 배분하는 과정입니다. 더 좋은 방법이 있을것 같은데 슬랙에 올려주시면 감사하겠어요
        if j < len(sorted_dic)/10 :
            dic_rank.append([sorted_dic[j][0]+1, 'A+'])
        elif j < len(sorted_dic)*2/10:
            dic_rank.append([sorted_dic[j][0]+1, 'A0'])
        elif j < len(sorted_dic)*3/10:
            dic_rank.append([sorted_dic[j][0]+1, 'A-'])
        elif j < len(sorted_dic)*4/10:
            dic_rank.append([sorted_dic[j][0]+1,'B+'])
        elif j < len(sorted_dic)*5/10:
            dic_rank.append([sorted_dic[j][0]+1,'B0'])
        elif j < len(sorted_dic)*6/10:
            dic_rank.append([sorted_dic[j][0]+1,'B-'])
        elif j < len(sorted_dic)*7/10:
            dic_rank.append([sorted_dic[j][0]+1,'C+'])
        elif j < len(sorted_dic)*8/10:
            dic_rank.append([sorted_dic[j][0]+1,'C0'])
        elif j < len(sorted_dic)*9/10:
            dic_rank.append([sorted_dic[j][0]+1,'C-'])
        else :
            dic_rank.append([sorted_dic[j][0]+1,'D0'])
    for k in range(len(dic_rank)):  # 대상을 찾아 학점을 뽑아오는 과정입니다.
        if dic_rank[k][0] == which :
            result = dic_rank[k][1]

    print(f'#{i+1} {result}')

        

# python Level2_1983.py
