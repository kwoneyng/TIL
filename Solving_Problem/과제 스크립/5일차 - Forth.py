for T in range(int(input())):
    n = input().split()
    stack = []
    print('#{} '.format(T+1), end='')
    for i in n:
        if len(stack) >= 2:
            if i == '+':
                a = stack.pop() + stack.pop()
                stack.append(a)
            elif i == '-':
                a = stack.pop(-2) - stack.pop(-1)
                stack.append(a)
            elif i == '*':
                a = stack.pop() * stack.pop()
                stack.append(a)
            elif i == '/':
                a = stack.pop(-2) // stack.pop(-1)
                stack.append(a)
            elif i == '.':
                print('error')
                break
            else :
                stack.append(int(i))
        else :
            if i == '.' and len(stack) == 1:
                print(stack.pop())
            elif i.isdigit() :
                stack.append(int(i))
            else :
                print('error')
                break