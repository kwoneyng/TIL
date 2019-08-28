ls = ['+', '-', '*', '/']

for T in range(10):
    n = int(input())
    data = '(' + input() + ')'
    stack = []
    calc = []
    su = []
    yun = []
    
    
    for i in data:
        chk = ''
        if i != ')':
            calc.append(i)
        else :
            while chk != '(':
                chk = calc.pop()
                if chk in ls:
                    yun.append(chk)
                elif chk == '(':
                    pass
                else :
                    su.append(chk)
        j = 0
        while yun.count('*'):
            if yun[j] == '*' :
                yun.pop(j)
                num2 = int(su.pop(j))
                num1 = int(su.pop(j))
                su.insert(j, num1 * num2)
                j -= 1
            j += 1
        j = 0
        while yun:
            yun.pop()
            num2 = int(su.pop())
            num1 = int(su.pop())
            su.append(num1+num2) 
        if len(su) == 1:
            a = su.pop()
            calc.append(str(a))
    print('#{} '.format(T+1), end='')
    print(calc[0])
