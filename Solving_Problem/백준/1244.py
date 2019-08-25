no = int(input())
light = list(map(int, input().split()))
std = int(input())
std_set = []
for i in range(std):
    std_set.append(list(map(int, input().split())))
for i in std_set:
    if i[0] == 1:
        for j in range(1, len(light) + 1):
            a = i[1]*j - 1
            if a >= 0 and a < len(light):
                if light[a] == 0:
                    light[a] = 1
                else :
                    light[a] = 0
    else :
        for j in range(len(light)):
            c = i[1]-j-1
            d = i[1]+j-1
            if c >= 0 and d < len(light):
                if light[c] == light[d]:
                    if light[c] == 0:
                        light[c] = 1
                        light[d] = 1
                    else :
                        light[c] = 0
                        light[d] = 0
                else :
                    break
j = 0
for i in range(len(light)//20):
   status_now = ' '.join(map(str,light[20*i:20*i+20]))
   print(status_now)
   j = 20*(i+1)
status_now = ' '.join(map(str, light[j:]))
print(status_now)