
def solution(A, B, C, D):
    vis = [0,0,0,0]
    su = [A,B,C,D]
    result = set()
    def perm(ls=[]):
        if sum(vis) == 4:
            if ls[0] > 2:
               return
            elif ls[0] == 2:
                if ls[1] > 4:
                    return
                elif ls[2] > 5:
                    return
                else:
                    result.add(''.join(map(str,ls)))
            elif ls[2] > 5:
                return
            else:
                result.add(''.join(map(str,ls)))
        for i in range(4):
            if vis[i] == 0:
                vis[i] = 1
                perm(ls+[su[i]])
                vis[i] = 0
    perm()
    print(len(result))

a,b,c,d = map(int, input().split())
solution(a,b,c,d)
