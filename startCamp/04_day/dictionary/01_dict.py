lunch1 = {
    '중국집' : '02'
}
lunch2 = dict(중국집='02')

print(lunch1)
print(lunch2)

lunch1['분식집'] = '031'

idol = {
    'bts' : { 
        '지민' : 24,
        'RM' : 25
    }
}
print(idol)
print(idol['bts']['RM'])

print('=========================================')
for key in lunch1:
    print(key,lunch1[key])   #for문을 돌릴때 Key값을 뽑아오고 키를 넣으면 value가 나옴
for value in lunch1.values():
    print(value)
for key in lunch1.keys():
    print(key)
# .items() => kye, value 가져오기
for key, value in lunch1.items():
    print(lunch1.items)
    print(key, value)
