def cumsum(t):
    cum = []
    for n, i in enumerate(t):
        cum.append(sum(t[:n + 1]))
    return(cum)
