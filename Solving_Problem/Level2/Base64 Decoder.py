import base64

for i in range(int(input())):
    a = input()
    b = base64.b64decode(a)
    c = b.decode('UTF-8')
    print(f'#{i+1} {c}')