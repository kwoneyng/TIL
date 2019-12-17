from collections    import deque
def swp():
    if len(a) < 2:
        return 1
    a[-1], a[-2] = a[-2], a[-1]

a = deque([1,3])
swp()
print(a)
