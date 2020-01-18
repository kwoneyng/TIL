import sys

ht = {}
cnt = 0
while True:
    a = input()
    if not a:
        break
    cnt += 1
    else:
        if ht.get(a) :
            ht[a] += 1
        else:
            ht[a] = 1
print(ht)
for name, percent in ht.items():
    print(f'{name} {map(percent/cnt)}')