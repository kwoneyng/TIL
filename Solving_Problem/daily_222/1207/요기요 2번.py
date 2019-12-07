def solution(s):
    rs = list(''.join(''.join(s.split()).split('-')))
    result = ''
    if len(rs)%3 == 1:
        flag = 0
        for i in range(len(rs)):
            for i in range(3):
                if len(rs) == 2:
                    break
                result += rs.pop(0)
            else:
                result += '-'
        result += '-'
        for i in range(2):
            result += rs.pop(0)
    else:
        for i in range(len(rs)):
            for i in range(3):
                if len(rs) == 0:
                    break
                result += rs.pop(0)
            else:
                result += '-'
    a=list(result)
    if a[-1] == '-':
        a.pop()
    return ''.join(a)


s = input()
print(solution(s))