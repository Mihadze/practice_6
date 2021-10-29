def nested_sum(t):
    a = []
    for i in range(t):
        a.append([int(j) for j in input("Введите вложенный список:").split()])
    for p in range(t):
        a[p] = sum(a[p])
    a = sum(a)
    print(a)
    
    



