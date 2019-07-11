"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
sum = 0
for i in score :
    sum = sum + score[i]
print(round(sum/len(score)))





# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
sum_a = 0
sum_b = 0
avg_a = 0
avg_b =0
for i in scores['a'] :
    sum_a = sum_a + scores['a'][i]
for i in scores['b'] :
    sum_b = sum_b + scores['b'][i]
avg_a = sum_a/len(scores['a'])
avg_b = sum_b/len(scores['b'])
print(f'A반 평균 = {avg_a} B반 평균 = {avg_b} 전체 평균 = {(avg_a+avg_b)/2}')



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
S_s = 0
S_d = 0
S_g = 0
S_b = 0
A_s = 0
A_d = 0
A_g = 0
A_b = 0
for i in range(len(city['서울'])) :
    S_s += city['서울'][i]
for i in range(len(city['대전'])) :
    S_d += city['대전'][i]
for i in range(len(city['광주'])) :
    S_g += city['광주'][i]
for i in range(len(city['부산'])) :
    S_b += city['부산'][i]
A_s = S_s/len(city['서울'])
A_d = S_d/len(city['대전'])
A_g = S_g/len(city['광주'])
A_b = S_b/len(city['부산'])


print(f'서울 : {round(A_s,2)}\n대전 : {round(A_d,2)}\n광주 : {round(A_g,2)}\n부산 : {round(A_b,2)}')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""





# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
min = 0
max = 0
n_p = ''
x_p = ''
for i in city :
    for j in city[i] :
        if j < min :
            min = j
    for j in city[i] :
        if j > max :
            max = j
print(min)
print(max)  
for i in city :
    if min in city[i] :
        n_p = i
for i in city :
    if max in city[i] :
        x_p = i
print(n_p)
print(x_p)

print(f'가장 추웠던 곳 : {n_p}\n가장 더웠던 곳 : {x_p}')





# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
YoN = 0
for i in range(len(city['서울'])):
    if city['서울'][i] == 2 :
        YoN = 1

# 아래에 코드를 작성해 주세요.
if YoN == 1 :
    print('Yes')
else :
    print('No')