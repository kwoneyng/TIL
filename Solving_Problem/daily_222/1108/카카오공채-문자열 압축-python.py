def solution(s):
    answer = 10000
    for dan in range(1,len(s)//2+2):
        q = []
        st = ''
        for i in range(len(s)//dan):
            q.append(''.join(s[i*dan:(i+1)*dan]))
        rem = ''.join(s[(i+1)*dan:])
        if rem:
            q.append(rem)
        rs = 1
        rst = ''
        for i in range(len(q)):
            rss = q[i]
            if i+1 < len(q) and q[i] == q[i+1]:
                rs += 1
            elif rs > 1:
                rst = rst + str(rs) + rss
                rs = 1
            else :
                rst = rst + rss
        answer = min(answer, len(rst))
    
    return answer