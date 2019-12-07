def solution(S):
    ls = list(S)
    wdset = []
    vis = []
    for i in range(len(ls)):
        if ls[i] not in vis:
            vis.append(ls[i])
        else:
            wdset.append(vis)
            vis = [ls[i]]
    wdset.append(vis)
    return(len(wdset))
S = input()
print(solution(S))