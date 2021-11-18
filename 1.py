def nested_sum(t):
    summ = 0
    for i in t:
        summ += sum(i)
    return(summ)
