#
print(__name__)
def mysum(num):
    if num == 1:
        return 1
    return num + mysum(num-1)
n = mysum(3)
print(n)