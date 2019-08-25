for T in range(10):
    stack = []
    n = int(input())
    st = input()
    rs = 0
    for i in st:
        if i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        elif i == '{':
            stack.append('}')
        elif i == '<':
            stack.append('>')
        elif i == ')':
            if stack.pop() == ')':
                continue
            else :
                rs == 0
                break
        elif i == '}':
            if stack.pop() == '}':
                continue
            else : 
                rs = 0
                break
        elif i == ']':
            if stack.pop() == ']':
                continue
            else:
                rs = 0
                break
        elif i == '>':
            if stack.pop() == '>':
                continue
            else :
                rs = 0
                break
    if len(stack) == 0 :
        rs = 1
    print(f'#{T+1} ',end='')
    print(rs)
