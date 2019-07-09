dinner = {
'양자강' : '02-557-4211', # 차돌짬뽕
'김밥카페' : '02-553-3181', # 라돈
'순남시래기' : '02-508-0887', # 보쌈정식
}
# dinner.keys() : key값만 list형태로
# dinner.values() : value값만 list형태로

# # 1. String formatting
# with open('dinner.csv', 'w', encoding="utf-8") as f :
    
#     for item in dinner.items() : #딕셔너리를 아이템으로 만들수 있음 ex) [['양자강','02-557-4221'],'['김밥카페','02-553-3181'], ...]
#         f.write(f'{item[0]},{item[1]}\n')

# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f : # newline = '' 새로운 줄로 바뀔 때 아무것도 없는 옵션으로 바꿈 # 옵션으로 줄 때는 공백 없이
    csv_writer = csv.writer(f) # f 라는 파일에 csv 를 작성하는 객체를 생성
    for item in dinner.items() :
        csv_writer.writerow(item)
        # 항상 파일 마지막에는 빈줄 하나를 남겨줌