from collections import deque

def num(x):
    stack.append(x)

def pop():
    stack.pop()

def inv():
    a = stack.pop()
    stack.append(-a)

def dup():
    stack.append(stack[-1])

def swp():
    if len(stack) < 2:
        return 1
    stack[-1], stack[-2] = stack[-2], stack[-1]

def add():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if a+b > 1000000000:
        return 1
    stack.append(a+b)

def sub():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if b-a < -1000000000:
        return 1
    stack.append(b-a)

def mul():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if a*b > abs(1000000000):
        return 1
    stack.append(a*b)

def div():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    if a == 0:
        return 1
    b = stack.pop()
    stack.append(b//a)

def mod():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    if a == 0:
        return 1
    b = stack.pop()
    stack.append(b%a)


while True:
    func = []
    cmd = input()
    cnt = 0
    if cmd == "QUIT":
        break
    elif cmd != "END":
        cnt += 1
        func.append(cmd)
    else:
        stack = deque()
        error = 0
        for i in range(cnt):
            stack.append(int(input()))
            for cmd in func:
                if cmd[:3] == 'NUM':
                    if num(int(cmd[-1])) == 1:
                        break
                elif cmd[:3] == 'POP':
                    if pop() == 1:
                        break
                elif cmd[:3] == 'INV':
                    error = inv()
                elif cmd[:3] == 'DUP':
                    error = dup()
                elif cmd[:3] == 'SWP':
                    error = swp()
                elif cmd[:3] == 'ADD':
                    error = add()
                elif cmd[:3] == 'SUB':
                    error = sub()
                elif cmd[:3] == 'MUL':
                    error = mul()
                elif cmd[:3] == 'DIV':
                    error = div()
                elif cmd[:3] == 'MOD':
                    error = mod()
            