import operator

test_num = int(input())
for i in range(test_num):
    a = list(map(int, input().split()))
    pp = a[0]
    which = a[1]
    score_set = []
    dic_stu = {}
    dic_rank = []
    result = ''
    for j in range(pp):
        score_set = list(map(int, input().split()))
        dic_stu[j] = round(0.35*score_set[0]+0.45*score_set[1]+0.2*score_set[2],2)
    sorted_dic = sorted(dic_stu.items(), key=operator.itemgetter(1),reverse=True)
    for j in range(len(sorted_dic)):
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
    for k in range(len(dic_rank)):
        if dic_rank[k][0] == which :
            result = dic_rank[k][1]

    print(f'#{i+1} {result}')

        

# python Level2_1983.py
