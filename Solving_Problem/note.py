t_s = list(map(str, [11*i for i in range(1,10)]))
t_s.append('00')

s = '1238099084'
# for i in t_s:
#     if i in s:
#         s.replace(i,'')
#     else :
#         print(s)
s.replace('99', '0',1)
print(s)