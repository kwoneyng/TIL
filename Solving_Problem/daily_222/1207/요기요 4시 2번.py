def solution(A):
    word = list(A)
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            word.pop(i)
            break
    else:
        word.pop()
    print(''.join(word))
    return ''.join(word)



A = input()
solution(A)