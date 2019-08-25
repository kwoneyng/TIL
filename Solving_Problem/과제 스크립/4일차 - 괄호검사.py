for T in range(int(input())):
    stack = []
    st = input()
    rs = 0
    for i in st:
        if len(stack) == 0 :
            if i == ')' or i == '}':
                rs = 0
                break
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '}':
            if stack.pop() == '}':
                rs = 1
                continue
            else :
                rs = 0
                break
        elif i == ')':
            if stack.pop() == ')':
                rs = 1
                continue
            else :
                rs = 0
                break
    if len(stack) != 0 :
        rs = 0
    print(f'#{T+1} ',end='')
    print(rs)
    