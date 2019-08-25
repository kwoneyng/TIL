for T in range(int(input())):
    kind, limit = list(map(int, input().split()))
    food =[]
    for i in range(kind):
        food.append(list(map(int, input().split())))
    print(food)
    kcal = [0]*(limit+1)
    for i in food:
        kcal[i[1]] = i[0]
    print(kcal)
    cals = [i[1] for i in food]
    # for i in range(1001):
    print(cals)