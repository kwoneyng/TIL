from collections import deque

def num(x):
    if abs(x) > 1e9:
        return 1
    stack.append(x)

def pop():
    if stack:
        stack.pop()
    else:
        return 1

def inv():
    if stack:
        a = stack.pop()
        stack.append(-a)
    else:
        return 1
def dup():
    if stack:
        stack.append(stack[-1])
    else: return 1

def swp():
    if len(stack) < 2:
        return 1
    stack[-1], stack[-2] = stack[-2], stack[-1]

def add():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(a+b) > 1e9:
        return 1
    stack.append(a+b)

def sub():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(b-a) > 1e9:
        return 1
    stack.append(b-a)

def mul():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(a*b) > 1e9:
        return 1
    stack.append(a*b)

def div():
    buho = 0
    if len(stack) < 2:
        return 1
    a = stack.pop()
    if a == 0:
        return 1
    b = stack.pop()
    if a < 0 :
        buho += 1
    if b < 0 :
        buho += 1
    if buho % 2 == 0:
        bu = 1
    else: 
        bu = -1
    stack.append(abs(b)//abs(a)*bu)

def mod():
    buho = 0
    if len(stack) < 2:
        return 1
    a = stack.pop()
    if a == 0:
        return 1
    b = stack.pop()
    if b < 0 :
        buho += 1
    if buho % 2 == 0:
        bu = 1
    else: 
        bu = -1
    stack.append(abs(b)%abs(a)*bu)

stop = 0
while True:
    if stop == 1:
        break
    else:
        func = deque()
        while True:
            cmd = input()
            if cmd == "QUIT":
                stop = 1
                break
            elif cmd != "END":
                func.append(cmd)
            else:
                for i in range(int(input())):
                    stack = deque()
                    error = 0
                    stack.append(int(input()))
                    for cmd in func:
                        if cmd[:3] == 'NUM':
                            if num(int(cmd[4:])) == 1:
                                break
                        elif cmd[:3] == 'POP':
                            if pop() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'INV':
                            if inv() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'DUP':
                            if dup() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'SWP':
                            if swp() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'ADD':
                            if add() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'SUB':
                            if sub() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'MUL':
                            if mul() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'DIV':
                            if div() == 1:
                                error = 1
                                break
                        elif cmd[:3] == 'MOD':
                            if mod() == 1:
                                error = 1
                                break
                    else:
                        if len(stack) != 1:
                            error = 1
                    if error == 0:
                        print(stack.pop())
                    else:
                        print('ERROR')
                print(input())
                func = deque()

# NUM -4
# DIV
# END
# 2
# 13
# -13

# NUM 4
# DIV
# END
# 2
# 13
# -13

# NUM -4
# MOD
# END
# 2
# 13
# -13

# NUM 4
# MOD
# END
# 2
# 13
# -13

# QUIT