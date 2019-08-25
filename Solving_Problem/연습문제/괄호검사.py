st1 = '()()((()))'
st2 = '((()((((()()((()())((())))))'
stack = [0]*15
top = -1
for i in st1:
    print(stack, top)
    if i == '(':
        top += 1
        stack[top] = ')'
    elif i == ')':
        if stack[top] == ')':
            top -= 1
        else :
            print('ERROR!!')
            break
if top != -1:
    print('ERROR')

for i in st2:
    print(stack, top)
    if i == '(':
        top += 1
        stack[top] = ')'
    elif i == ')':
        if stack[top] == ')':
            top -= 1
        else :
            print('ERROR!!')
            break
if top != -1:
    print('ERROR')